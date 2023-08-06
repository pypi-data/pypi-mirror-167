################################################################################
# File: /deepeye/d01_pre_processing/services/initialise_srv.py                 #
# Project: deep_eye_no_dementia                                                #
# File Created: Wednesday, 11th May 2022 1:27:52 am                            #
# Author: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                           #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 11th May 2022 1:27:52 am                           #
# Modified By: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                      #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d_utils.runtime_context import RuntimeContext

from ...d_utils.enums import *
from ...d_utils import logger
from pathlib import Path
import os


def initialise_pre_processor(rc: RuntimeContext):
    from ..model.contextmodel import PreProcessingContext

    logger.info("initializing pre_processing")

    my_pre_processor_context = PreProcessingContext()
    data_access_data_sets = rc.config.get_data_sets()
    pre_processing_data_sets = rc.config.get_data_sets(step=Step.pre_processed)

    my_pre_processor_context.data_sets = [
        da_ds
        for pp_ds in pre_processing_data_sets
        for da_ds in data_access_data_sets
        if da_ds.name == pp_ds
    ]
    my_pre_processor_context.data_browser = rc.data_browser
    my_pre_processor_context.mode = rc.config.get_mode(Step.pre_processed)
    my_pre_processor_context.development_state = rc.config.get_development_state()
    my_pre_processor_context.null_strategy = rc.config.get_null_strategy()
    try:
        my_pre_processor_context.check_it()
        my_pre_processor_context.make_it()
    except Exception as e:
        raise e

    rc.pre_processing_context = my_pre_processor_context

    Path(rc.pre_processing_context.get_datasets_path()).mkdir(
        parents=True, exist_ok=True
    )

    os.environ["TFDS_DATA_DIR"] = rc.pre_processing_context.get_datasets_path()
    return rc
