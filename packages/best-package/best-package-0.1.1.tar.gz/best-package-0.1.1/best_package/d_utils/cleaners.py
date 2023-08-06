from ..d_utils.runtime_context import RuntimeContext
from ..d_utils.enums import *
import shutil
import os
from pathlib import Path


def clear_last_run_data(rc: RuntimeContext, step: Step):
    if step not in [Step.modelled, Step.outputted]:
        raise RuntimeError("There is no run folder for %s" % step.name)

    if step == Step.modelled:
        last_run_dir = rc.data_browser.run_modelling_path(
            rc.modelling_context.mode, rc.modelling_context.last_run_name
        )
    else:
        last_run_dir = rc.data_browser.run_output_path(
            rc.modelling_context.mode, rc.modelling_context.last_run_name
        )

    if os.path.isdir(last_run_dir):
        shutil.rmtree(last_run_dir)
    # delete run folder if empty
    last_run_dir_path = Path(last_run_dir).parent
    is_empty = Path(last_run_dir_path).is_dir() and not any(
        Path(last_run_dir_path).iterdir()
    )
    if is_empty:
        shutil.rmtree(str(last_run_dir_path))

    return
