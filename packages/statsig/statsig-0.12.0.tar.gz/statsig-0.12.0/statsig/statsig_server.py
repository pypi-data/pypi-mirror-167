import dataclasses
import json
import logging
import threading
from typing import Optional
from statsig.layer import Layer
from statsig.statsig_errors import StatsigNameError, StatsigRuntimeError, StatsigValueError
from statsig.statsig_event import StatsigEvent
from statsig.statsig_metadata import _StatsigMetadata

from statsig.statsig_user import StatsigUser
from .statsig_error_boundary import _StatsigErrorBoundary
from .evaluator import _ConfigEvaluation, _Evaluator
from .statsig_network import _StatsigNetwork
from .statsig_logger import _StatsigLogger
from .dynamic_config import DynamicConfig
from .statsig_options import StatsigOptions
from .version import __version__

RULESETS_SYNC_INTERVAL = 10
IDLISTS_SYNC_INTERVAL = 60


class StatsigServer:
    _errorBoundary: _StatsigErrorBoundary

    def __init__(self) -> None:
        self._errorBoundary = _StatsigErrorBoundary()

    def initialize(self, sdkKey: str, options=None):
        if sdkKey is None or not sdkKey.startswith("secret-"):
            raise StatsigValueError(
                'Invalid key provided.  You must use a Server Secret Key from the Statsig console.')
        if options is None:
            options = StatsigOptions()
        self._errorBoundary.set_api_key(sdkKey)

        try:
            self._options = options
            self.__shutdown_event = threading.Event()
            self.__statsig_metadata = _StatsigMetadata.get()
            self._network = _StatsigNetwork(sdkKey, options)
            self._logger = _StatsigLogger(
                self._network, self.__shutdown_event, self.__statsig_metadata, self._errorBoundary, options.local_mode,
                options.event_queue_size)
            self._evaluator = _Evaluator()

            self._last_update_time = 0

            if not options.local_mode:
                if options.bootstrap_values is not None:
                    self._bootstrap_config_specs()
                else:
                    self._download_config_specs()
                self.__background_download_configs = threading.Thread(
                    target=self._sync,
                    args=(self._download_config_specs, options.rulesets_sync_interval or RULESETS_SYNC_INTERVAL,))
                self.__background_download_configs.daemon = True
                self.__background_download_configs.start()

            if not options.local_mode:
                self._download_id_lists()
                self.__background_download_idlists = threading.Thread(
                    target=self._sync,
                    args=(self._download_id_lists, options.idlists_sync_interval or IDLISTS_SYNC_INTERVAL,))
                self.__background_download_idlists.daemon = True
                self.__background_download_idlists.start()

            self._initialized = True
        except (StatsigValueError, StatsigNameError, StatsigRuntimeError) as e:
            raise e
        except Exception as e:
            self._errorBoundary.log_exception(e)
            self._initialized = True

    def check_gate(self, user: StatsigUser, gate_name: str):
        def task():
            if not self._verify_inputs(user, gate_name):
                return False

            result = self.__check_gate_server_fallback(user, gate_name)
            return result.boolean_value

        return self._errorBoundary.capture(task, lambda: False)

    def get_config(self, user: StatsigUser, config_name: str):
        def task():
            if not self._verify_inputs(user, config_name):
                return DynamicConfig({}, config_name, "")

            result = self.__get_config_server_fallback(user, config_name)
            return DynamicConfig(result.json_value, config_name, result.rule_id)

        return self._errorBoundary.capture(task, lambda: DynamicConfig({}, config_name, ""))

    def get_experiment(self, user: StatsigUser, experiment_name: str):
        def task():
            return self.get_config(user, experiment_name)

        return self._errorBoundary.capture(task, lambda: DynamicConfig({}, experiment_name, ""))

    def get_layer(self, user: StatsigUser, layer_name: str) -> Layer:
        def task():
            if not self._verify_inputs(user, layer_name):
                return Layer._create(layer_name, {}, "")

            normal_user = self.__normalize_user(user)
            result = self._evaluator.get_layer(normal_user, layer_name)
            result = self.__resolve_eval_result(
                normal_user, layer_name, result=result, log_exposure=True, is_layer=True)

            def log_func(layer: Layer, parameter_name: str):
                self._logger.log_layer_exposure(
                    normal_user, layer, parameter_name, result)

            return Layer._create(
                layer_name,
                result.json_value,
                result.rule_id,
                log_func
            )

        return self._errorBoundary.capture(task, lambda: Layer._create(layer_name, {}, ""))

    def log_event(self, event: StatsigEvent):
        def task():
            if not self._initialized:
                raise StatsigRuntimeError(
                    'Must call initialize before checking gates/configs/experiments or logging events')

            event.user = self.__normalize_user(event.user)
            self._logger.log(event)

        self._errorBoundary.swallow(task)

    def shutdown(self):
        def task():
            self.__shutdown_event.set()
            self._logger.shutdown()
            if not self._options.local_mode:
                self.__background_download_configs.join()
                self.__background_download_idlists.join()

        self._errorBoundary.swallow(task)

    def override_gate(self, gate: str, value: bool, user_id: Optional[str] = None):
        self._errorBoundary.swallow(
            lambda: self._evaluator.override_gate(gate, value, user_id))

    def override_config(self, config: str, value: object, user_id: Optional[str] = None):
        self._errorBoundary.swallow(
            lambda: self._evaluator.override_config(config, value, user_id))

    def override_experiment(self, experiment: str, value: object, user_id: Optional[str] = None):
        self._errorBoundary.swallow(
            lambda: self._evaluator.override_config(experiment, value, user_id))

    def get_client_initialize_response(self, user: StatsigUser):
        def task():
            return self._evaluator.get_client_initialize_response(self.__normalize_user(user))

        def recover():
            return None

        return self._errorBoundary.capture(task, recover)

    def evaluate_all(self, user: StatsigUser):
        def task():
            all_gates = dict()
            for gate in self._evaluator.get_all_gates():
                result = self.__check_gate_server_fallback(user, gate, False)
                all_gates[gate] = {
                    "value": result.boolean_value,
                    "rule_id": result.rule_id
                }

            all_configs = dict()
            for config in self._evaluator.get_all_configs():
                result = self.__get_config_server_fallback(user, config, False)
                all_configs[config] = {
                    "value": result.json_value,
                    "rule_id": result.rule_id
                }
            return dict({
                "feature_gates": all_gates,
                "dynamic_configs": all_configs
            })

        def recover():
            return dict({
                "feature_gates": dict(),
                "dynamic_configs": dict()
            })

        return self._errorBoundary.capture(task, recover)

    def _verify_inputs(self, user: StatsigUser, variable_name: str):
        if not self._initialized:
            raise StatsigRuntimeError(
                'Must call initialize before checking gates/configs/experiments or logging events')
        if not user or (not user.user_id and not user.custom_ids):
            raise StatsigValueError(
                'A non-empty StatsigUser with user_id or custom_ids is required. See https://docs.statsig.com/messages/serverRequiredUserID')
        if not variable_name:
            return False

        return True

    def __check_gate_server_fallback(self, user: StatsigUser, gate_name: str, log_exposure=True):
        user = self.__normalize_user(user)
        result = self._evaluator.check_gate(user, gate_name)
        if result.fetch_from_server:
            network_gate = self._network.post_request("check_gate", {
                "gateName": gate_name,
                "user": user.to_dict(True),
                "statsigMetadata": self.__statsig_metadata,
            })
            if network_gate is None:
                return _ConfigEvaluation()
            return _ConfigEvaluation(boolean_value=network_gate.get("value"), rule_id=network_gate.get("rule_id"))
        elif log_exposure:
            self._logger.log_gate_exposure(
                user, gate_name, result.boolean_value, result.rule_id, result.secondary_exposures)
        return result

    def __get_config_server_fallback(self, user: StatsigUser, config_name: str, log_exposure=True):
        user = self.__normalize_user(user)

        result = self._evaluator.get_config(user, config_name)
        return self.__resolve_eval_result(user, config_name, result, log_exposure, False)

    def __resolve_eval_result(self, user, config_name: str, result: _ConfigEvaluation, log_exposure, is_layer):
        if result.fetch_from_server:
            network_config = self._network.post_request("get_config", {
                "configName": config_name,
                "user": user.to_dict(True),
                "statsigMetadata": self.__statsig_metadata,
            })
            if network_config is None:
                return _ConfigEvaluation()

            return _ConfigEvaluation(json_value=network_config.get("value", {}),
                                     rule_id=network_config.get("ruleID", ""))
        elif log_exposure:
            if not is_layer:
                self._logger.log_config_exposure(
                    user, config_name, result.rule_id, result.secondary_exposures)
        return result

    def __normalize_user(self, user):
        userCopy = dataclasses.replace(user)
        if self._options is not None and self._options._environment is not None:
            userCopy._statsig_environment = self._options._environment
        return userCopy

    def _sync(self, sync_func, interval):
        while True:
            try:
                if self.__shutdown_event.wait(interval):
                    break
                sync_func()
            except Exception as e:
                self._errorBoundary.log_exception(e)

    def _bootstrap_config_specs(self, ):
        if self._options.bootstrap_values is None:
            return
        try:
            specs = json.loads(self._options.bootstrap_values)
            self.__save_json_config_specs(specs)
        except ValueError:
            # JSON deconding failed, just let background thread update rulesets
            logging.getLogger('statsig.sdk').exception(
                'Failed to parse bootstrap_values')
            return

    def __save_json_config_specs(self, specs, notify=False):
        if specs is None:
            return
        time = specs.get("time")
        if time is not None:
            self._last_update_time = time
        if specs.get("has_updates", False):
            self._evaluator.set_downloaded_configs(specs)
            if callable(self._options.rules_updated_callback):
                self._options.rules_updated_callback(json.dumps(specs))

    def _download_config_specs(self):
        specs = self._network.post_request("download_config_specs", {
            "statsigMetadata": self.__statsig_metadata,
            "sinceTime": self._last_update_time,
        })
        self.__save_json_config_specs(specs, True)

    def _download_id_list(self, url, list_name, local_list, all_lists, start_index):
        resp = self._network.get_request(
            url, headers={"Range": "bytes=%s-" % start_index})
        if resp is None:
            return
        try:
            content_length_str = resp.headers.get('content-length')
            if content_length_str is None:
                raise StatsigValueError("Content length invalid.")
            content_length = int(content_length_str)
            content = resp.text
            if content is None:
                return
            first_char = content[0]
            if first_char != "+" and first_char != "-":
                raise StatsigNameError("Seek range invalid.")
            lines = content.splitlines()
            for line in lines:
                if len(line) <= 1:
                    continue
                op = line[0]
                id = line[1:].strip()
                if op == "+":
                    local_list.get("ids", set()).add(id)
                elif op == "-":
                    local_list.get("ids", set()).discard(id)
            local_list["readBytes"] = start_index + content_length
            all_lists[list_name] = local_list
        except Exception as e:
            self._errorBoundary.log_exception(e)

    def _download_id_lists(self):
        try: 
            server_id_lists = self._network.post_request("get_id_lists", {
                "statsigMetadata": self.__statsig_metadata,
            })
            if server_id_lists is None:
                return

            local_id_lists = self._evaluator.get_id_lists()
            thread_pool = []

            for list_name in server_id_lists:
                server_list = server_id_lists.get(list_name, dict())
                url = server_list.get("url", None)
                size = server_list.get("size", 0)
                local_list = local_id_lists.get(list_name, dict())

                new_creation_time = server_list.get("creationTime", 0)
                old_creation_time = local_list.get("creationTime", 0)
                new_file_id = server_list.get("fileID", None)
                old_file_id = local_list.get("fileID", "")

                if url is None or new_creation_time < old_creation_time or new_file_id is None:
                    continue

                # should reset the list if a new file has been created
                if new_file_id != old_file_id and new_creation_time >= old_creation_time:
                    local_list = {
                        "ids": set(),
                        "readBytes": 0,
                        "url": url,
                        "fileID": new_file_id,
                        "creationTime": new_creation_time,
                    }
                    
                read_bytes = local_list.get("readBytes", 0)
                # check if read bytes count is the same as total file size; only download additional ids if sizes don't match
                if size <= read_bytes or url == "":
                    continue
                thread = threading.Thread(
                    target=self._download_id_list, args=(url, list_name, local_list, local_id_lists, read_bytes, ))
                thread.daemon = True
                thread_pool.append(thread)
                thread.start()

            for thread in thread_pool:
                thread.join()

            deleted_lists = []
            for list_name in local_id_lists:
                if list_name not in server_id_lists:
                    deleted_lists.append(list_name)

            # remove any list that has been deleted
            for list_name in deleted_lists:
                local_id_lists.pop(list_name, None)
        except Exception as e:
            self._errorBoundary.log_exception(e)
