################################################################################
# File: /best_package/d02_modelling/services/finalizing_srv.py                 #
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 5:41:00 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 5:41:00 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d_utils.runtime_context import RuntimeContext
from ...d_utils import logger
import pickle
from ...d_utils import file_names


def run(rc: RuntimeContext):
    logger.info("finalizing modelling step")
    where_to_save = rc.modelling_context.get_modelling_folder_path()
    full_path = where_to_save + file_names.modelling_context_file_name(
        rc.modelling_context.current_run_name
    )
    with open(full_path, "wb") as handle:
        pickle.dump(rc.modelling_context, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return rc
