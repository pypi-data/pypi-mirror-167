################################################################################
# File: __init__.py                                                            #
# Path: \__init__.py                                                           #
# File Created: Saturday, 4th January 2020 2:47:44 pm                          #
# Author: Zaher Joukhadar                                                      #
# zjoukhadar@unimelb.edu.au                                                    #
# ---------------------------------------------------------------              #
# Last Modified: Tuesday, 7th January 2020 5:21:01 pm                          #
# Modified By: Zaher Joukhadar                                                 #
# zjoukhadar@unimelb.edu.au                                                    #
# ---------------------------------------------------------------              #
# Copyright 2019 - 2020, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
import os

import sys
import pathlib as pl
from .d_utils import logger
from .d_utils.enums import *
from pathlib import Path
from pyfiglet import Figlet
from termcolor import colored


def initialise():
    f = Figlet(font="slant")
    print(colored(f.renderText(get_package_name()), color="green"))
    from .d_utils import package_initializer

    print("Initializing %s" % get_package_name())
    path = Path(os.path.abspath(sys.argv[0])).parents[0]

    try:
        package_initializer.run(path)
        print("%s has been initialized" % get_package_name())
    except Exception as e:
        print(e.__str__())
    return


def start(is_on_spartan: bool = False):
    from .d_utils import tools as tl
    from . import best_package_engine

    from .d_utils.runtime_context import RuntimeContext

    if not is_on_spartan:
        os.environ["XLA_FLAGS"] = "--xla_force_host_platform_device_count=32"
    else:
        import tensorflow as tf

        tf.config.experimental.set_visible_devices([], "GPU")

    path = ""
    is_running_in_notebook = tl.isnotebook()
    if is_running_in_notebook:

        path = Path(os.getcwd()).parents[0]

        # tl.copy_config_file_when_run_in_notebook(Config_type.base)
        # tl.copy_config_file_when_run_in_notebook(Config_type.local)
    else:
        path = Path(os.path.abspath(sys.argv[0])).parents[0]

    try:
        runtime_context = RuntimeContext(
            execuation_path=path, is_notebook=is_running_in_notebook
        )
        runtime_context.is_running_on_spartan = is_on_spartan
        runtime_context.run_configuration()
        best_package_engine.start(runtime_context)

        return runtime_context
    except Exception as e:
        logger.error(e.__str__())


def run(runtime_context):
    from . import best_package_engine

    logger.info("running %s engine" % get_package_name())
    best_package_engine.run(runtime_context)


def run_data_sync(runtime_context):
    from . import best_package_engine

    logger.info("running data sync")
    best_package_engine.run_data_sync(runtime_context)


def run_on_spartan(runtime_context):
    from . import best_package_engine

    logger.info("generating and submitting job to spartan")
    best_package_engine.run_on_spartan(runtime_context)


def get_version():
    return __version__


def get_package_name():
    folder_path = os.path.dirname(__file__)
    package_name = os.path.basename(folder_path)
    return package_name


__version__ = "0.0.1.dev"
