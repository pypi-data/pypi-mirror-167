################################################################################
# File: /modeller.py                                                           #
# Project: d03_modelling                                                       #
# File Created: Sunday, 10th October 2021 4:23:36 am                           #
# Author: Ubuntu# zjoukhadar@unimelb.edu.au                                    #
# ---------------------------------------------------------------              #
# Last Modified: Sunday, 10th October 2021 4:23:36 am                          #
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
        rc = initialise_srv.initialise_modeller(rc)
    except Exception as e:
        logger.exception("initializing modelling step failed. %s" % e.__str__())
        raise e
    if rc.config.is_pipeline_step_enabled(Step.modelled):
        logger.info("modelling is enabled")

        try:
            rc = finalizing_srv.run(rc)
        except Exception as e:
            logger.exception("finalising modelling step failed. %s" % e.__str__())
            raise e
        logger.info("modelling finished running...")
    else:
        logger.info("modelling step is disabled")

    return rc
