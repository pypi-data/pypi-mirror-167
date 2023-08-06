################################################################################
# File: /best_package/d02_modelling/services/deeplearning_srv.py               #
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 7:44:39 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 7:44:39 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from ...d_utils.runtime_context import RuntimeContext


import numpy as np


from ..model.my_trainer import train_and_evaluate
from ..model.hyper_parameters import HyperParameters


def run(rc: RuntimeContext):
    import tensorflow_datasets as tfds
    import jax

    db = tfds.builder("dataset01_dataset", rc=rc)
    dataset = db.as_dataset(split=tfds.split_for_jax_process("dataset01"))
    train_size = int(1 - rc.modelling_context.test_size * len(dataset))
    val_size = int(rc.modelling_context.test_size * len(dataset))

    dataset = dataset.shuffle(buffer_size=10, reshuffle_each_iteration=False)

    train_dataset = dataset.take(train_size)
    val_dataset = dataset.skip(train_size)
    val_dataset = dataset.take(val_size)

    per_device_batch_size = rc.modelling_context.per_device_batch_size

    per_host_batch_size = per_device_batch_size * jax.local_device_count()

    train_dataset = train_dataset.batch(per_host_batch_size, drop_remainder=False)
    test_dataset = test_dataset.batch(per_host_batch_size, drop_remainder=False)

    hps = HyperParameters()
    hps.number_epochs = rc.modelling_context.number_epochs
    hps.num_classes = rc.modelling_context.number_classes
    hps.patch_size = rc.modelling_context.patch_size
    hps.num_channels = rc.modelling_context.number_channels

    model, results = train_and_evaluate(
        hyper_parameters=hps,
        runtime_context=rc,
        train_dataset=train_dataset,
        val_dataset=val_dataset,
    )
    return rc
