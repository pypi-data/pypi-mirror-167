################################################################################
# File: /data_access.py                                                        #
# Project: d00_data_access                                                     #
# File Created: Sunday, 10th October 2021 4:22:52 am                           #
# Author: Ubuntu# zjoukhadar@unimelb.edu.au                                    #
# ---------------------------------------------------------------              #
# Last Modified: Sunday, 10th October 2021 4:22:52 am                          #
# Modified By: Ubuntu# zjoukhadar@unimelb.edu.au                               #
# ---------------------------------------------------------------              #
# Copyright 2021 - 2021, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ..d_utils import logger
from ..d_utils.runtime_context import RuntimeContext
from .services import spartan_mrc_data_sync_srv
from .services import initialise_srv


def run(rc: RuntimeContext):
    logger.info("running data_access")
    try:
        rc = initialise_srv.initialise_data_access(rc)
    except Exception as e:
        logger.exception("initializing data access has failed. %s" % e.__str__())
        raise e
    return rc


def run_data_sync(rc: RuntimeContext):
    spartan_mrc_data_sync_srv.execute_data_sync(rc)
