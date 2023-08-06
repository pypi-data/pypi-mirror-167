################################################################################
# File: /enums.py                                                              #
# Project: d_utils                                                             #
# File Created: Sunday, 10th October 2021 4:15:22 am                           #
# Author: Ubuntu# zjoukhadar@unimelb.edu.au                                    #
# ---------------------------------------------------------------              #
# Last Modified: Sunday, 10th October 2021 4:15:22 am                          #
# Modified By: Ubuntu# zjoukhadar@unimelb.edu.au                               #
# ---------------------------------------------------------------              #
# Copyright 2021 - 2021, Melbourne Data Analytics Platform (MDAP)              #
################################################################################
from enum import Enum


class Config_type(Enum):
    local = 1
    base = 2


class Step(Enum):
    data_access = 0
    pre_processed = 1
    modelled = 2
    outputted = 3


class Method(Enum):
    isomap = 1
    method01 = 2
    VisionTransformer = 3
    Conv2D = 4
    Conv3D = 5


class Problem_type(Enum):
    classification = 0
    segmentation = 0
    regression = 0


class Mode(Enum):
    development = 0
    production = 1


class Development_state(Enum):
    skeleton = 0
    in_progress = 2
    released = 1


class DataSetFormat(Enum):
    csv = 0
    images = 1
