################################################################################
# File: /best_package/d_utils/package_initializer.py                           #
# Project: best_project                                                        #
# File Created: Friday, 9th September 2022 3:36:40 am                          #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Friday, 9th September 2022 3:36:41 am                         #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from pathlib import Path
import os
from ..d_utils.enums import *
import yaml
import sys
from datetime import datetime
from . import tools as tl


def config_generator(conf_type: Config_type):
    conf = {}
    if conf_type == Config_type.base:
        conf = {
            "control": {
                "method": "method01",
                "data_access": {"data_set": "dataset01", "data_set_format": "images"},
                "pre_processed": {"save_data": True, "enabled": False},
                "modelled": {
                    "clear_last_run_data": False,
                    "save_data": True,
                    "enabled": False,
                },
                "outputted": {
                    "clear_last_run_data": False,
                    "save_data": True,
                    "enabled": False,
                },
            }
        }
    else:
        conf = {
            "root_data_path": "/volume/data/",
            "mrc_data_dir": "/volume/data/",
            "spartan_data_dir": "/data/projects/punim1484/data/",
        }

    return conf


def initialize_config(execuation_path: Path):
    config_folder_path = Path(execuation_path / "conf")
    base_config_path = Path(config_folder_path / "base.yaml")
    local_config_path = Path(config_folder_path / "local.yaml")
    try:
        if not os.path.exists(base_config_path):
            Path(config_folder_path).mkdir(parents=True, exist_ok=True)
            print("generating new base config file at %s" % base_config_path)
            with open(base_config_path, "w") as base_config_file:
                yaml.dump(
                    config_generator(Config_type.base),
                    base_config_file,
                    default_flow_style=False,
                    sort_keys=False,
                )

        if not os.path.exists(local_config_path):
            Path(config_folder_path).mkdir(parents=True, exist_ok=True)
            print("generating new local file at %s" % local_config_path)
            with open(local_config_path, "w") as local_config_file:
                yaml.dump(
                    config_generator(Config_type.local),
                    local_config_file,
                    default_flow_style=False,
                    sort_keys=False,
                )
    except Exception as e:
        print(e.__str__())
    return True


def generate_first_notebook(notebook_folder_path: Path):
    import getpass

    import nbformat as nbf

    nb = nbf.v4.new_notebook()
    cells = []

    # Assume make_image() saves an image to file and returns the filename
    # image_file = make_image(var)
    text = "Hello"

    cell = nbf.v4.new_code_cell(
        source=[
            "import os",
            "import sys",
            "module_path = os.path.abspath(os.path.join('..'))",
            "sys.path.append(module_path)",
        ]
    )

    cell2 = nbf.v4.new_code_cell(
        source=["import best_package", "best_package.initialise()"]
    )

    cells.append(cell)
    cells.append(cell2)

    nb["cells"] = cells

    notebook_path = str(notebook_folder_path / "%s_%s_EDA.ipynb") % (
        datetime.now().strftime("%Y_%m_%d"),
        getpass.getuser(),
    )

    with open(str(notebook_path), "a+") as f:
        nbf.write(nb, f)

    return


def initialize_notebooks(execuation_path: Path):

    notebooks_path = execuation_path / "notebooks"

    if not os.path.exists(notebooks_path):
        print("making the notebooks folder at %s" % notebooks_path)
        Path(notebooks_path).mkdir(parents=True, exist_ok=True)
        generate_first_notebook(notebooks_path)
    else:
        notebook_folder_empty = True
        with os.scandir(notebooks_path) as it:
            if any(it):
                notebook_folder_empty = False
        if notebook_folder_empty:
            generate_first_notebook(notebooks_path)

    return


def run(execuation_path: Path):
    is_running_in_notebook = tl.isnotebook()
    if is_running_in_notebook:
        print("running in notebook")
        execuation_path = Path(os.getcwd()).parents[0]
    print("running from %s" % execuation_path)
    initialize_config(execuation_path=execuation_path)
    initialize_notebooks(execuation_path=execuation_path)
    return
