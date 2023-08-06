################################################################################
# File: /best_package/d00_data_access/model/contextmodel.py                    #
# Project: best_project                                                        #
# File Created: Friday, 9th September 2022 1:18:41 am                          #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Friday, 9th September 2022 1:18:41 am                         #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################

from .datamodel import *
from ...d_utils.enums import *
from typing import List
from ...d_utils.data_browser import DataBrowser
import os
import pathlib as pl


class DataAccessContext:
    data_sets: List[DataSet]
    data_browser: DataBrowser
    development_state: Development_state

    def __init__(self):
        pass

    def check_input_datasets_exist(self):
        for data_set in self.data_sets:
            data_path = self.data_browser.top_original_path(data_set=data_set)
            # check if there is data there
            data_size = 0
            for dirpath, dirnames, filenames in os.walk(data_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp):
                        data_size += os.path.getsize(fp)
            if data_size == 0:
                raise RuntimeError(
                    "data set %s is empty. Make sure that you have the original data for %s placed at %s"
                    % (data_set.name, data_set.name, data_path)
                )
        return True

    def make_working_folder(self):
        try:
            pl.Path(self.data_browser.top_working_path(mode=Mode.development)).mkdir(
                parents=True, exist_ok=True
            )
            pl.Path(self.data_browser.top_working_path(mode=Mode.production)).mkdir(
                parents=True, exist_ok=True
            )
        except Exception as e:
            raise e
        return 0

    def make_output_folder(self):
        try:

            pl.Path(self.data_browser.top_output_path(mode=Mode.development)).mkdir(
                parents=True, exist_ok=True
            )
            pl.Path(self.data_browser.top_output_path(mode=Mode.production)).mkdir(
                parents=True, exist_ok=True
            )
        except Exception as e:
            raise e
        return 0

    def run(self):
        if self.development_state != Development_state.skeleton:
            self.check_input_datasets_exist()
        return 0

    def make_it(self):
        self.make_output_folder()
        self.make_working_folder()
        return 0
