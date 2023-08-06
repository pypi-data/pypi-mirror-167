################################################################################
# File: /best_package/d01_pre_processing/services/finishing_srv.py             #
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 5:39:39 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 5:39:39 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d_utils.runtime_context import RuntimeContext
from ...d_utils import logger
import pickle
from ...d_utils import file_names


def run(rc: RuntimeContext):
    logger.info("finalizing pre_processing step")
    where_to_save = rc.pre_processing_context.get_working_data_path()
    full_path = where_to_save + file_names.pre_processing_context_file_name()
    with open(full_path, "wb") as handle:
        pickle.dump(rc.pre_processing_context, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return rc
