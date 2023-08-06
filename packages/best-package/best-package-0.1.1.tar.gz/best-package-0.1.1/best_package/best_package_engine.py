from glob import glob
from .d00_data_access import data_access
from .d01_pre_processing import pre_processor
from .d02_modelling import modeller
from .d03_outputting import outputter
from .d_utils import spartan
from .d_utils.runtime_context import RuntimeContext
from .d_utils import logger
import os


def start(rc: RuntimeContext):

    rc.write_to_runtime_data("engine_started", True)
    logger.info("%s engine has started" % get_package_name())


def run_data_sync(rc: RuntimeContext):
    data_access.run_data_sync(rc)


def run_on_spartan(rc: RuntimeContext):
    spartan.generate_and_submit_spartan_job(rc)


def run(rc: RuntimeContext):

    if rc.read_from_runtime_data("engine_started"):
        logger.info("%s engine is now running." % get_package_name())
        try:
            rc = data_access.run(rc)
            rc = pre_processor.run(rc)
            rc = modeller.run(rc)
            rc = outputter.run(rc)
        except Exception as e:
            logger.error(e.__str__())
            raise e

    else:
        logger.error(
            "Engine has not been started. Please start the engine before running it by calling start()"
        )


def get_package_name():
    folder_path = os.path.dirname(__file__)
    package_name = os.path.basename(folder_path)
    return package_name


if __name__ == "__main__":
    run()
