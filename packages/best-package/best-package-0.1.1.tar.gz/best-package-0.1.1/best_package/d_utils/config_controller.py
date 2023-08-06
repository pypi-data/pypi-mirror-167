from .enums import *
from ..d00_data_access.model.datamodel import DataSet
import yaml


class ConfigController:
    runtime_base_path: str
    runtime_local_path: str

    def __init__(self, runtime_base_path, runtime_local_path):
        self.runtime_base_path = runtime_base_path
        self.runtime_local_path = runtime_local_path

    def __get_config(self, config_type: Config_type):
        if config_type == Config_type.base:
            config_path = self.runtime_base_path
        if config_type == Config_type.local:
            config_path = self.runtime_local_path
        with open(config_path, "r") as f:
            conf = yaml.safe_load(f)
            return conf

    def is_pipeline_step_enabled(self, ps: Step):
        return self.__get_config(Config_type.base)["pipeline"][ps.name]["enabled"]

    def should_save_data(self, ps: Step):
        return self.__get_config(Config_type.base)["pipeline"][ps.name]["save_data"]

    def get_data_sets(self, step: Step = None):
        if step:
            return self.__get_config(Config_type.base)["pipeline"][step.name][
                "data_sets"
            ].split(",")

        else:
            return [
                DataSet(
                    name=item["data_set"]["name"],
                    is_in_separate_folder=item["data_set"]["is_in_separate_folder"],
                )
                for item in self.__get_config(Config_type.base)["pipeline"][
                    Step.data_access.name
                ]
            ]

    def get_mode(self, step: Step):
        return Mode[self.__get_config(Config_type.base)["pipeline"][step.name]["mode"]]

    def get_development_state(self):
        return Development_state[
            self.__get_config(Config_type.base)["pipeline"]["development_state"]
        ]

    def get_method(self, step: Step):
        return Method[
            self.__get_config(Config_type.base)["pipeline"][step.name]["method"]
        ]

    def should_clear_last_run(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "clear_last_run_data"
        ]

    def keep_this_run_data(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "keep_data_of_run_name"
        ]

    def should_clear_last_output(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.outputted.name][
            "clear_last_output_data"
        ]

    def should_split(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "should_split"
        ]

    def what_run_name_to_use_in_output(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.outputted.name][
            "use_modelling_run_name"
        ]

    def keep_this_output_data(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "keep_output_data_of"
        ]

    def get_problem_type(self):
        return Problem_type[
            self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
                "problem_type"
            ]
        ]

    def get_number_of_classes(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "number_classes"
        ]

    def get_number_of_channels(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "number_channels"
        ]

    def get_per_device_batch_size(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "per_device_batch_size"
        ]

    def get_patch_size(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "patch_size"
        ]

    def get_test_size(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "test_size"
        ]

    def get_number_epochs(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.modelled.name][
            "epochs"
        ]

    def get_null_strategy(self):
        return self.__get_config(Config_type.base)["pipeline"][Step.pre_processed.name][
            "null_strategy"
        ]

    def get_input_variables(self):
        return self.__get_variables(input=True)

    def get_target_variables(self):
        return self.__get_variables(input=False)

    #############################
    ########SETTINGS#############
    #############################

    def get_sync_settings_folder_names(self):
        return self.__get_config(Config_type.base)["settings"]["data_sync"][
            "folder_names"
        ].split(",")

    def get_sync_settings_from(self):
        return self.__get_config(Config_type.base)["settings"]["data_sync"]["from"]

    def get_sync_settings_to(self):
        return self.__get_config(Config_type.base)["settings"]["data_sync"]["to"]

    def get_spartan_user_name(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["user_name"]

    def get_spartan_conda_env(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["conda_env"]

    def get_spartan_qos_setting(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["qos"]

    def get_spartan_account(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["account"]

    def get_spartan_partition(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["partition"]

    def get_spartan_cpus_per_task(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"][
            "cpus_per_task"
        ]

    def get_spartan_gpus_per_node(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"][
            "gpus_per_node"
        ]

    def get_spartan_memory(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["memory"]

    def get_spartan_time_days(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["time"][
            "days"
        ]

    def get_spartan_time_hours(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["time"][
            "hours"
        ]

    def get_spartan_time_minutes(self):
        return self.__get_config(Config_type.base)["settings"]["spartan"]["time"][
            "minutes"
        ]

    def get_spartan_data_dir(self):
        return self.__get_config(Config_type.local)["spartan_data_dir"]

    def get_mrc_data_dir(self):
        return self.__get_config(Config_type.local)["mrc_data_dir"]
