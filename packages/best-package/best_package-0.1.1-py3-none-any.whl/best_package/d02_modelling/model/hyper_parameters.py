################################################################################
# File: /best_package/d02_modelling/model/hyper_parameters.py                  #
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 8:05:53 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 8:05:53 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from dataclasses import dataclass


@dataclass
class HyperParameters:
    embed_dim: int = 64
    hidden_dim: int = 512
    num_heads: int = 8
    num_layers: int = 6
    patch_size: int = 512
    num_channels: int = 1
    num_patches: int = 512
    num_classes: int = 2
    number_epochs: int = 200
    dropout_prob: float = 0.2
    learning_rate: float = 3e-4
    weight_decay: float = 0.01
