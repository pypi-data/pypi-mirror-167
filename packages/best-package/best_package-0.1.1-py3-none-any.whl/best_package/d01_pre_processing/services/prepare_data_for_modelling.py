################################################################################
# File: /best_package/d01_pre_processing/services/prepare_data_for_modelling.py#
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 7:19:24 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 7:19:24 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d_utils.runtime_context import RuntimeContext

from ...d00_data_access.datasets import dataset01_dataset


def run(rc: RuntimeContext):
    import tensorflow_datasets as tfds

    data_path = rc.pre_processing_context.get_working_data_path()
    dl_config = tfds.download.DownloadConfig(manual_dir=data_path + "metadata")
    db = tfds.builder("dataset01_dataset", rc=rc)
    db.download_and_prepare(download_config=dl_config)
    return rc
