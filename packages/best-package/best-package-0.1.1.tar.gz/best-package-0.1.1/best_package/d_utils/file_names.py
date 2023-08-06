################################################################################
# File: /best_package/d_utils/file_names.py                                    #
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 6:52:10 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 6:52:10 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from .constants import *


def modelling_context_file_name(run_name: str):
    return "modelling_context_" + run_name + CONTEXT_FILE_EXTENTION


def pre_processing_context_file_name():
    return "pre_processing_context" + CONTEXT_FILE_EXTENTION
