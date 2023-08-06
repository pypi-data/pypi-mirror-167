################################################################################
# File: /reportor.py                                                           #
# Project: d06_reporting                                                       #
# File Created: Sunday, 10th October 2021 4:24:08 am                           #
# Author: Ubuntu# zjoukhadar@unimelb.edu.au                                    #
# ---------------------------------------------------------------              #
# Last Modified: Sunday, 10th October 2021 4:24:08 am                          #
# Modified By: Ubuntu# zjoukhadar@unimelb.edu.au                               #
# ---------------------------------------------------------------              #
# Copyright 2021 - 2021, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ..d_utils import logger

from ..d_utils.runtime_context import RuntimeContext
from ..d_utils.enums import Step
from .services import initialise_srv, finalizing_srv


def run(rc: RuntimeContext):
    try:
        rc = initialise_srv.initialise_outputting(rc)
    except Exception as e:
        logger.exception("initializing outputting step failed. %s" % e.__str__())
        raise e
    if rc.config.is_pipeline_step_enabled(Step.outputted):
        logger.info("outputting is enabled")

        try:
            rc = finalizing_srv.run(rc)
        except Exception as e:
            logger.exception("finalising outputting step failed. %s" % e.__str__())
            raise e
        logger.info("outputting finished running...")
    else:
        logger.info("outputting step is disabled")

    return rc
