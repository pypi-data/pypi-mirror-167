################################################################################
# File: /deepeye/d00_data_arc.configess/services/spartan_mrc_data_sync_srv.py         #
# Project: deep_eye_no_dementia                                                #
# File Created: Wednesday, 11th May 2022 1:53:29 am                            #
# Author: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                           #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 11th May 2022 1:53:29 am                           #
# Modified By: Zaher Joukhadar# zjoukhadar@unimelb.edu.au                      #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d_utils import logger
import subprocess
from ...d_utils.runtime_context import RuntimeContext
import getpass
from ... import get_version


def constrcut_command_list(rc: RuntimeContext):

    source = rc.config.get_sync_settings_from()
    dest = rc.config.get_sync_settings_to()
    list_folders = rc.config.get_sync_settings_folder_names()
    list_commands = []
    source_data_path = ""
    dest_data_path = ""
    spartan = rc.config.get_spartan_data_dir()
    mrc = rc.config.get_mrc_data_dir()
    if spartan == "":
        logger.error(
            "Spartan data location is not provided. Make sure the key 'spartan_data_dir' in local.yaml is poiting to where the data is stored on spartan"
        )
        return 1
    if mrc == "":
        logger.error(
            "mrc data location is not provided. Make sure the key 'mrc_data_dir' in local.yaml is poiting to where the data is stored on mrc vm"
        )
        return 1

    if source == "spartan":
        source_data_path = rc.config.get_spartan_data_dir()
        if dest == "mrc":
            dest_data_path = rc.config.get_mrc_data_dir()
        for fn in list_folders:
            # if fn == 'original': continue
            list_commands.append(
                "rsync -avz  "
                + rc.config.get_spartan_user_name()
                + "@spartan.hpc.unimelb.edu.au:"
                + source_data_path
                + "/"
                + fn
                + " "
                + dest_data_path
                + "/"
            )
        return list_commands
    if dest == "spartan":
        if source == "mrc":
            source_data_path = rc.config.get_mrc_data_dir()
        dest_data_path = rc.config.get_spartan_data_dir()
        for fn in list_folders:
            # if fn == 'original': continue
            # list_commands.append(
            # "rsync -avz  "
            # + rc.config.get_spartan_user_name()
            # + "@spartan.hpc.unimelb.edu.au:"
            # + source_data_path
            # + "/"
            # + fn
            # + " "
            # + dest_data_path
            # + "/"
            # )
            list_commands.append(
                "rsync -avz  "
                + source_data_path
                + getpass.getuser()
                + "/deepeye/"
                + get_version()
                + "/"
                + fn
                + "/oct/02_processed/datasets"
                + " "
                + rc.config.get_spartan_user_name()
                + "@spartan.hpc.unimelb.edu.au:"
                + dest_data_path
                + "derived/oct/02_processed/"
            )
        return list_commands


def run_command(command):
    completed = subprocess.run(command, shell=True)
    print("returncode:", completed.returncode)
    return


def execute_data_sync(rc: RuntimeContext):
    # rc.config.save_run_time_configs()
    source = rc.config.get_sync_settings_from()
    dest = rc.config.get_sync_settings_to()
    list_folders = rc.config.get_sync_settings_folder_names()
    if source == "spartan":
        source_path = rc.config.get_spartan_data_dir()
        dest_path = rc.config.get_mrc_data_dir()
    if source == "mrc":
        source_path = rc.config.get_mrc_data_dir()
        dest_path = rc.config.get_spartan_data_dir()

    logger.info(
        "Moving data from folders %s at %s in %s to %s at %s"
        % (" ".join(list_folders), source_path, source, dest, dest_path)
    )
    command_list = constrcut_command_list(rc)
    if command_list == 1:
        return
    for comm in command_list:
        run_command(comm)
