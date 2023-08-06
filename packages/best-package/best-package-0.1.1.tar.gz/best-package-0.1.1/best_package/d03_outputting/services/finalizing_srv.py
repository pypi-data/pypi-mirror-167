################################################################################
# File: /best_package/d03_outputting/services/finalizing_srv.py                #
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 5:45:31 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 5:45:31 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d_utils.runtime_context import RuntimeContext
from ...d_utils import logger


def run(rc: RuntimeContext):
    logger.info("finalizing outputting step")
    return rc
