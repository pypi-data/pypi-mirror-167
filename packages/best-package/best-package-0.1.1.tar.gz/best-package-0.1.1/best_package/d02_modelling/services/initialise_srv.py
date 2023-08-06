import imp
from ...d_utils.runtime_context import RuntimeContext
from ...d_utils.cleaners import clear_last_run_data

from ...d_utils import logger
from ...d_utils.enums import *
import os


def initialise_modeller(rc: RuntimeContext):
    logger.info("initialising modelling step")

    from ..model.contextmodel import ModellingContext

    last_run_name = rc.get_previous_run_name(Step.modelled)
    if last_run_name is None or last_run_name == 0:
        current_run_name = "run_01"
    else:
        current_run_name = "run_" + str(int(last_run_name[4:]) + 1)
    rc.set_current_run_name(current_run_name, Step.modelled)
    my_modelling_context = ModellingContext(current_run_name, last_run_name)
    my_modelling_context.mode = rc.config.get_mode(Step.modelled)
    my_modelling_context.data_browser = rc.data_browser
    my_modelling_context.development_state = rc.config.get_development_state()
    my_modelling_context.test_size = rc.config.get_test_size()
    my_modelling_context.problem_type = rc.config.get_problem_type()
    my_modelling_context.number_classes = rc.config.get_number_of_classes()
    my_modelling_context.number_epochs = rc.config.get_number_epochs()
    my_modelling_context.per_device_batch_size = rc.config.get_per_device_batch_size()
    my_modelling_context.patch_size = rc.config.get_patch_size()
    my_modelling_context.number_channels = rc.config.get_number_of_channels()
    data_access_data_sets = rc.config.get_data_sets()
    modelling_data_sets = rc.config.get_data_sets(step=Step.modelled)

    my_modelling_context.data_sets = [
        da_ds
        for pp_ds in modelling_data_sets
        for da_ds in data_access_data_sets
        if da_ds.name == pp_ds
    ]

    my_modelling_context.method = rc.config.get_method(Step.modelled)

    logger.info(
        "current modelling run name: %s using %s"
        % (current_run_name, my_modelling_context.method.name)
    )

    try:
        my_modelling_context.check_it()
        my_modelling_context.make_it()
    except Exception as e:
        raise e
    rc.modelling_context = my_modelling_context

    if (
        rc.config.should_clear_last_run()
        and last_run_name != rc.config.keep_this_run_data()
    ):
        clear_last_run_data(rc, Step.modelled)

    os.environ["TFDS_DATA_DIR"] = rc.pre_processing_context.get_datasets_path()

    return rc
