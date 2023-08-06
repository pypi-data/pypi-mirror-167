################################################################################
# File: /deepeye/d06_reporting/services/initialise_srv.py                      #
# Project: deep_eye_no_dementia                                                #
# File Created: Friday, 20th May 2022 6:00:08 am                               #
# Author: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                           #
# ---------------------------------------------------------------              #
# Last Modified: Friday, 20th May 2022 6:00:08 am                              #
# Modified By: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                      #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d_utils.runtime_context import RuntimeContext
from ...d_utils import logger
from ...d_utils.enums import *
from ...d_utils.cleaners import clear_last_run_data
import pickle
from ...d_utils import file_names


def initialise_outputting(rc: RuntimeContext):
    from ..model.contextmodel import OutputtingContext

    logger.info("initialising outputting step")
    last_run_name = rc.get_previous_run_name(Step.outputted)
    modeller_run_name = rc.config.what_run_name_to_use_in_output()

    rc.set_current_run_name(modeller_run_name, Step.outputted)

    my_outputting_context = OutputtingContext(
        modeller_run_name=modeller_run_name, last_run_name=last_run_name
    )

    my_outputting_context.data_browser = rc.data_browser
    my_outputting_context.mode = rc.config.get_mode(Step.outputted)
    my_outputting_context.development_state = rc.config.get_development_state()

    data_access_data_sets = rc.config.get_data_sets()
    outputting_data_sets = rc.config.get_data_sets(step=Step.outputted)

    my_outputting_context.data_sets = [
        da_ds
        for pp_ds in outputting_data_sets
        for da_ds in data_access_data_sets
        if da_ds.name == pp_ds
    ]

    logger.info("output using run name: %s" % (modeller_run_name))

    try:
        my_outputting_context.run()
        my_outputting_context.make_it()
    except Exception as e:
        raise e
    rc.outputting_context = my_outputting_context
    if (
        rc.config.should_clear_last_output()
        and last_run_name != rc.config.keep_this_output_data()
    ):
        clear_last_run_data(rc, Step.outputted)

    # retrieve modelling context
    context_file_path = rc.modelling_context.get_modelling_folder_path(
        modeller_run_name
    ) + file_names.modelling_context_file_name(modeller_run_name)

    with open(context_file_path, "rb") as handle:
        rc.modelling_context = pickle.load(handle)
    return rc
