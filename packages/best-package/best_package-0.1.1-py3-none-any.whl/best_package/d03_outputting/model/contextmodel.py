################################################################################
# File: /best_package/d03_outputting/model/__pycache__/contextmodel.py         #
# Project: best_project                                                        #
# File Created: Friday, 9th September 2022 6:19:47 am                          #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Friday, 9th September 2022 6:19:47 am                         #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################

from ...d_utils.enums import Development_state, Method, Mode
from ...d00_data_access.model.datamodel import *
from typing import List
from ...d_utils.data_browser import DataBrowser
import os
import pathlib as pl


class OutputtingContext:
    data_sets: List[DataSet]
    data_browser: DataBrowser
    modeller_run_name: str
    last_run_name: str
    mode: Mode
    method: Method
    development_state: Development_state

    def __init__(self, modeller_run_name: str, last_run_name):
        self.modeller_run_name = modeller_run_name
        self.last_run_name = last_run_name
        pass

    def check_modelled_data_exist(self):

        data_path = self.data_browser.run_modelling_path(
            self.mode, self.modeller_run_name
        )
        # check if there is data there
        data_size = 0
        for dirpath, dirnames, filenames in os.walk(data_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    data_size += os.path.getsize(fp)
        if data_size == 0:
            raise RuntimeError(
                "modelled data for %s is empty. Make sure that you have the data for modelled %s placed at %s"
                % (self.modeller_run_name, self.modeller_run_name, data_path)
            )
        return True

    def make_outputting_folder(self):
        try:
            for data_set in self.data_sets:
                pl.Path(
                    self.data_browser.run_output_path(
                        self.mode, self.modeller_run_name, data_set
                    )
                ).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise e
        return 0

    def run(self):
        if self.development_state != Development_state.skeleton:
            self.check_modelled_data_exist()
        return True

    def make_it(self):
        self.make_outputting_folder()

        return 0
