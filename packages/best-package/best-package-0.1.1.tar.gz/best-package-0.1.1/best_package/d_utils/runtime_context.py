################################################################################
# File: /configration.py                                                       #
# Project: d_utils                                                             #
# File Created: Monday, 12th April 2021 4:53:20 am                             #
# Author: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                           #
# ---------------------------------------------------------------              #
# Last Modified: Monday, 12th April 2021 4:53:21 am                            #
# Modified By: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                      #
# ---------------------------------------------------------------              #
# Copyright 2021 - 2021, Melbourne Data Analytics Platform (MDAP)              #
################################################################################

import logging
from datetime import datetime

from .enums import Config_type, Method,  Step
from . import logger
import pathlib as pl
import yaml

import getpass
import shutil
from .. import get_version
from .. import get_package_name
import glob
import os
from .config_controller import ConfigController
from .data_browser import DataBrowser
from ..d00_data_access.model.contextmodel import DataAccessContext
from ..d01_pre_processing.model.contextmodel import PreProcessingContext
from ..d02_modelling.model.contextmodel import ModellingContext
from ..d03_outputting.model.contextmodel import OutputtingContext




class RuntimeContext:

    runtime_tag: str
    root_data_path: str
    original_data_path: str
    execution_path: str
    log_path: str
    is_notebook: bool
    package_name: str
    config: ConfigController
    data_browser: DataBrowser
    data_access_context : DataAccessContext
    pre_processing_context: PreProcessingContext
    modelling_context : ModellingContext
    outputting_context : OutputtingContext

    is_running_on_spartan: bool
    def __init__(self, execuation_path: str, is_notebook: bool):
        self.runtime_tag = (
            get_version() + "_" + datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
        )
        self.execution_path = execuation_path
        self.is_notebook = is_notebook
        self.package_name = get_package_name()
        self.is_running_on_spartan = False
        self.store_execution_path()

        self.copy_runtime_base_config_file()

        self.copy_runtime_local_config_file()

        local_config_path = self.get_runtime_local_config_file_path()

        with open(local_config_path, "r") as f:
            local_conf = yaml.safe_load(f)
            self.original_data_path = local_conf["original_data_path"]
            self.root_data_path = local_conf["root_data_path"]

        self.config = ConfigController(self.get_runtime_base_config_file_path(), self.get_runtime_local_config_file_path())

  
        try:
            self.data_browser = DataBrowser(
                original_data_path= self.original_data_path, root_data_path= self.root_data_path
                )
        except Exception as e:
            logger.exception(e)
    
    def run_configuration(self):

        self.setup_logger()
    
        return

    def setup_logger(self):
        import jax
        logger = logging.getLogger(self.package_name)
        #logger.setLevel(logging.DEBUG)
        # We only want one process per machine to log things on the screen
        logger.setLevel(logging.INFO if jax.process_index() == 0 else logging.ERROR)
        formatter = logging.Formatter(
            "[%(asctime)s|%(levelname)s|%(processName)s|%(threadName)s| %(message)s"
        )

        handler = logging.FileHandler(self.get_log_file_path())
        stout_handler = logging._StderrHandler(logging.DEBUG)
        stout_handler.setFormatter(formatter)
        handler.setFormatter(formatter)

        # this bit will make sure we won't have
        # duplicated messages in the output
        if not len(logger.handlers):
            logger.addHandler(handler)
            logger.addHandler(stout_handler)

    def store_execution_path(self):
        with open(self.get_runtime_data_file_path(), "w") as file:
            documents = yaml.dump({"package_execution_path": str(self.execution_path)}, file)

    def get_runtime_data_file_path(self):
        return self.get_runtime_package_data_dir_path() + "/runtime_data.yml"

    def get_runtime_package_data_dir_path(self):
        curr_user_home_dir = str(pl.Path.home())
        package_data_dir_path = (
            curr_user_home_dir + "/."+self.package_name+"_package_data/" + self.runtime_tag
        )
        pl.Path(package_data_dir_path).mkdir(parents=True, exist_ok=True)
        return package_data_dir_path

    def get_log_file_path(self):
        log_dir_path = str(pl.Path.home()) + "/."+self.package_name+"_package_data/" + "logs/"
        pl.Path(log_dir_path).mkdir(parents=True, exist_ok=True)
        return log_dir_path + self.package_name+".%s" % self.runtime_tag + ".log"


   
    
    
    def copy_runtime_base_config_file(self):
        try:
            with open(
                self.get_package_execution_path() + "/conf/base.yaml"
            ) as yamlfile:
                base_config = yaml.safe_load(yamlfile)
                if base_config:
                    with open(
                        self.get_runtime_package_data_dir_path() + "/base.yaml", "w"
                    ) as yamlfile:
                        yaml.safe_dump(base_config, yamlfile)
        except Exception as e:
            logger.exception(
                "No base.yaml was found. Please create base.yaml at /conf/base.yaml. See documentation for more info."
            )
            raise e

    def copy_runtime_local_config_file(self):
        try:
            with open(
                self.get_package_execution_path() + "/conf/local.yaml"
            ) as yamlfile:
                local_config = yaml.safe_load(yamlfile)
                if local_config:
                    with open(
                        self.get_runtime_package_data_dir_path() + "/local.yaml", "w"
                    ) as yamlfile:
                        yaml.safe_dump(local_config, yamlfile)
        except Exception as e:
            logger.exception(
                "No local.yaml was found. Please create local.yaml at /conf/local.yaml. See documentation for more info."
            )
            raise e

    def get_runtime_base_config_file_path(self):
        return self.get_runtime_package_data_dir_path() + "/base.yaml"

    def get_runtime_local_config_file_path(self):
        return self.get_runtime_package_data_dir_path() + "/local.yaml"

    def get_package_execution_path(self):
        try:
            with open((self.get_runtime_data_file_path()), "r") as stream:
                try:
                    app_data = yaml.safe_load(stream)
                    return app_data["package_execution_path"]
                except yaml.YAMLError as exc:
                    logger.info(
                        "Cannot read runtime_data.yml file. Message: " + exc
                    )
        except FileNotFoundError as fnf_error:
            logger.exception(fnf_error)

    def write_to_runtime_data(self, key, value):
        try:
            with open((self.get_runtime_data_file_path()), "r") as stream:
                app_data = yaml.safe_load(stream)
                app_data[key] = value
            with open((self.get_runtime_data_file_path()), "w") as stream:
                yaml.safe_dump(app_data, stream)
        except FileNotFoundError as fnf_error:
            logger.exception(fnf_error)

    def read_from_runtime_data(self, key):
        try:
            with open((self.get_runtime_data_file_path()), "r") as stream:
                app_data = yaml.safe_load(stream)
                return app_data[key]
        except FileNotFoundError as fnf_error:
            logger.exception(fnf_error)

    def clean(self):
        # remove temporary app data when this run is finished
        try:
            shutil.rmtree(self.get_runtime_package_data_dir_path())
            # remove test logs
            if hasattr(self, "root_data_path"):
                if self.root_data_path.endswith("test/"):
                    shutil.rmtree(self.root_data_path)
            log_dir_path = str(pl.Path.home()) + "/."+self.package_name+"_package_data/" + "logs/"
            for f in glob.glob(log_dir_path + "*_test.log"):
                os.remove(f)
        except Exception as e:
            logger.exception(e)

    

    def get_previous_run_name(self, step: Step):
        try:
            #pick the lasted package app run time data
            curr_user_home_dir = str(pl.Path.home())
            package_data_dir_path = curr_user_home_dir + "/."+self.package_name+"_package_data/"
            sortedList = sorted(glob.glob(os.path.join(package_data_dir_path, '[!logs]*/')), key=os.path.getmtime)
            if len(sortedList) > 1:
                for i in range(len(sortedList) +1 ):
                    if i < 2:
                        continue
                    else:
                        pre_path = sortedList[-i] + "runtime_data.yml"
                        try:
                            with open(pre_path, "r") as stream:
                                app_data = yaml.safe_load(stream)
                                if step.name+"_run_name" in app_data:
                                    return app_data[step.name+"_run_name"]
                        except FileNotFoundError as fnf_error:
                            continue
                return 0
            else:
                return 0
        except Exception as e:  
            logger.exception(e)
            return 0

    def get_current_run_name(self, step: Step):
        try:
            #pick the lasted package app run time data
            with open((self.get_runtime_data_file_path()), "r") as stream:
                app_data = yaml.safe_load(stream)
                if not step.name+"_run_name" in app_data:
                    return 0
                else:
                    return app_data[step.name+"_run_name"]
        except FileNotFoundError as fnf_error:
            logger.exception(fnf_error)
            return 0

    def set_current_run_name(self, run_name: str, step: Step):
        try:
            with open((self.get_runtime_data_file_path()), "r") as stream:
                app_data = yaml.safe_load(stream)
                app_data[step.name+"_run_name"] = run_name
            with open((self.get_runtime_data_file_path()), "w") as stream:
                yaml.safe_dump(app_data, stream)
        except FileNotFoundError as fnf_error:
            logger.exception(fnf_error)
    
   