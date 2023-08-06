################################################################################
# File: /pre_processor.py                                                      #
# Project: d01_pre_processing                                                  #
# File Created: Sunday, 10th October 2021 4:23:01 am                           #
# Author: Ubuntu# zjoukhadar@unimelb.edu.au                                    #
# ---------------------------------------------------------------              #
# Last Modified: Sunday, 10th October 2021 4:23:01 am                          #
# Modified By: Ubuntu# zjoukhadar@unimelb.edu.au                               #
# ---------------------------------------------------------------              #
# Copyright 2021 - 2021, Melbourne Data Analytics Platform (MDAP)              #
################################################################################

from ..d_utils import logger
from ..d_utils.runtime_context import RuntimeContext
from ..d_utils.enums import Step, Development_state
from .services import (
    initialise_srv,
    finalizing_srv,
    null_strategy_srv,
    prepare_data_for_modelling,
)
from ..d_utils.enums import Step
from ..d00_data_access.services import data_savers, data_getters


def run(rc: RuntimeContext):
    try:
        rc = initialise_srv.initialise_pre_processor(rc)
    except Exception as e:
        logger.exception("initializing pre_processing step failed. %s" % e.__str__())
        raise e
    if rc.config.is_pipeline_step_enabled(Step.pre_processed):
        logger.info("pre_processing is enabled")
        logger.info("pre_processing started running...")
        try:
            rc = null_strategy_srv.run(rc)
            if (
                rc.pre_processing_context.development_state
                != Development_state.skeleton
            ):
                rc = prepare_data_for_modelling.run(rc)
            rc = finalizing_srv.run(rc)
        except Exception as e:
            logger.exception("finalising pre_processing step failed. %s" % e.__str__())
            raise e
        logger.info("pre_processing finished running...")
        return rc
    else:
        logger.info("pre_processing step is disabled")
        return rc


def move_data_to_general(rc: RuntimeContext):

    return
