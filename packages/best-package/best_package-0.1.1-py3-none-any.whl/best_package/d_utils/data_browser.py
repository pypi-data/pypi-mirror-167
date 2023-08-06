################################################################################
# File: /data_browser.py                                                       #
# Project: d_utils                                                             #
# File Created: Sunday, 10th October 2021 9:10:48 am                           #
# Author: Ubuntu# zjoukhadar@unimelb.edu.au                                    #
# ---------------------------------------------------------------              #
# Last Modified: Sunday, 10th October 2021 9:10:49 am                          #
# Modified By: Ubuntu# zjoukhadar@unimelb.edu.au                               #
# ---------------------------------------------------------------              #
# Copyright 2021 - 2021, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from .enums import Step, Method, Mode
import getpass
from .. import get_version, get_package_name
from ..d00_data_access.model.datamodel import DataSet
from pathlib import Path


class DataBrowser:
    original_data_path: str
    root_data_path: str

    method: Method

    def __init__(
        self,
        original_data_path: str,
        root_data_path: str,
    ):
        self.root_data_path = root_data_path
        self.original_data_path = original_data_path

    def top_original_path(self, data_set: DataSet):
        if data_set.is_in_separate_folder:
            return self.original_data_path + data_set.name
        else:
            return self.original_data_path

    def top_working_path(self, mode: Mode):
        top_user_working_path = (
            self.root_data_path
            + ((getpass.getuser() + "/") if mode == Mode.development else "")
            + get_package_name()
            + "/"
            + str(get_version())
            + "/working/"
        )
        return top_user_working_path

    def step_working_path(self, step: Step, mode: Mode, data_set: DataSet = None):
        step_user_working_path = (
            self.top_working_path(mode=mode)
            + step.name
            + "/"
            + (data_set.name + "/" if data_set else "")
        )
        return step_user_working_path

    def run_modelling_path(
        self,
        mode: Mode,
        run_name: str,
        data_set: DataSet = None,
    ):
        run_user_working_path = (
            self.step_working_path(Step.modelled, mode, data_set) + run_name + "/"
        )
        return run_user_working_path

    def top_output_path(self, mode: Mode):
        top_output_path = (
            self.root_data_path
            + ((getpass.getuser() + "/") if mode == Mode.development else "")
            + "/"
            + get_package_name()
            + "/"
            + str(get_version())
            + "/output/"
        )
        return top_output_path

    def run_output_path(self, mode: Mode, run_name: str, data_set: DataSet = None):
        run_output_path = (
            self.top_output_path(mode=mode)
            + run_name
            + "/"
            + (data_set.name + "/" if data_set else "")
        )
        return run_output_path
