################################################################################
# File: /deepeye/d01_pre_processing/model/contextmodel.py                      #
# Project: deep_eye_no_dementia                                                #
# File Created: Thursday, 14th July 2022 4:35:49 am                            #
# Author: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                           #
# ---------------------------------------------------------------              #
# Last Modified: Thursday, 14th July 2022 4:35:50 am                           #
# Modified By: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                      #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d00_data_access.model.datamodel import *
from typing import List
from ...d_utils.data_browser import DataBrowser
import os
import pathlib as pl
from ...d_utils.enums import *


class PreProcessingContext:

    data_sets: List[DataSet]
    data_browser: DataBrowser
    mode: Mode
    development_state: Development_state
    null_strategy: str

    def __init__(self):

        pass

    def make_preprocessing_folder(self):
        try:
            for data_set in self.data_sets:
                pl.Path(
                    self.data_browser.step_working_path(
                        Step.pre_processed, self.mode, data_set
                    )
                ).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise e
        return 0

    def get_working_data_path(self, data_set: DataSet = None):
        return self.data_browser.step_working_path(
            Step.pre_processed, self.mode, data_set
        )

    def get_datasets_path(self):
        return self.get_working_data_path() + "datasets"

    def check_it(self):

        # self.check_input_datasets_exist()

        return True

    def make_it(self):
        self.make_preprocessing_folder()
        return 0
