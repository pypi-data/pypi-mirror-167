################################################################################
# File: /tools.py                                                              #
# Project: d_utils                                                             #
# File Created: Sunday, 10th October 2021 4:10:22 am                           #
# Author: Ubuntu# zjoukhadar@unimelb.edu.au                                    #
# ---------------------------------------------------------------              #
# Last Modified: Sunday, 10th October 2021 4:10:22 am                          #
# Modified By: Ubuntu# zjoukhadar@unimelb.edu.au                               #
# ---------------------------------------------------------------              #
# Copyright 2021 - 2021, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
################################################################################
# File: /tools.py                                                              #
# Project: d_utils                                                             #
# File Created: Monday, 12th April 2021 4:13:37 am                             #
# Author: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                           #
# ---------------------------------------------------------------              #
# Last Modified: Monday, 12th April 2021 4:13:38 am                            #
# Modified By: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                      #
# ---------------------------------------------------------------              #
# Copyright 2021 - 2021, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
import multiprocessing, logging
from pathlib import Path
import os
from IPython import get_ipython
from ..d_utils.enums import *
import getpass
import yaml

from . import logger


def root():
    return str(Path(__file__).parent.parent.parent)


def isnotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


def save_context(context, step: Step):

    return


def get_context(step: Step, run_time: str = None):
    return


# region data_store tool functions:


# endregion


# endregion
