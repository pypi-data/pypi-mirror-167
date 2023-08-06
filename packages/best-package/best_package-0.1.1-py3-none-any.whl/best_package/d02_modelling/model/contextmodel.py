from ...d_utils.enums import Development_state, Method, Mode, Problem_type
from ...d00_data_access.model.datamodel import *
from typing import List
from ...d_utils.data_browser import DataBrowser
import os
import pathlib as pl


class ModellingContext:
    data_sets: List[DataSet]
    data_browser: DataBrowser
    current_run_name: str
    last_run_name: str
    mode: Mode
    method: Method
    development_state: Development_state
    test_size: float
    problem_type: Problem_type
    number_classes: int
    number_epochs: int
    per_device_batch_size: int
    patch_size: int
    number_channels: int

    def __init__(self, current_run_name: str, last_run_name: str):
        self.current_run_name = current_run_name
        self.last_run_name = last_run_name
        pass

    def make_modelling_folder(self):
        try:
            pl.Path(
                self.data_browser.run_modelling_path(self.mode, self.current_run_name)
            ).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise e
        return 0

    def get_modelling_folder_path(self, run_name: str = None):
        if run_name:
            temp_run_name = run_name
        else:
            temp_run_name = self.current_run_name
        return self.data_browser.run_modelling_path(self.mode, temp_run_name)

    def check_it(self):
        if self.development_state != Development_state.skeleton:
            pre_processed_data_path = (
                self.data_browser.step_working_path(Step.pre_processed, self.mode)
                + "datasets"
            )
            if not any(os.scandir(pre_processed_data_path)):
                raise RuntimeError(
                    "cannot do modelling, no pre-processed data found. Please run data pre-processing step first"
                )

            return True

    def make_it(self):
        self.make_modelling_folder()

        return 0
