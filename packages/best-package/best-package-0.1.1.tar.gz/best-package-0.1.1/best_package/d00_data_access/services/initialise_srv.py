################################################################################
# File: /best_package/d00_data_access/services/initialise_srv.py               #
# Project: best_project                                                        #
# File Created: Friday, 9th September 2022 2:06:00 am                          #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Friday, 9th September 2022 2:06:00 am                         #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################

from ...d_utils.runtime_context import RuntimeContext
from ...d_utils import logger


def initialise_data_access(rc: RuntimeContext):
    logger.info("initializing data_access")
    from ..model.contextmodel import DataAccessContext

    my_data_access_context = DataAccessContext()
    my_data_access_context.data_sets = rc.config.get_data_sets()
    my_data_access_context.data_browser = rc.data_browser
    my_data_access_context.development_state = rc.config.get_development_state()
    try:
        my_data_access_context.run()
        my_data_access_context.make_it()
    except Exception as e:
        raise e

    rc.data_access_context = my_data_access_context

    return rc
