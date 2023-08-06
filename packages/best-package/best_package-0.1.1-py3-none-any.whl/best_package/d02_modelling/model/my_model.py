################################################################################
# File: /best_package/d02_modelling/model/my_model.py                          #
# Project: best_project                                                        #
# File Created: Wednesday, 14th September 2022 8:22:23 am                      #
# Author: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                          #
# ---------------------------------------------------------------              #
# Last Modified: Wednesday, 14th September 2022 8:22:23 am                     #
# Modified By: Zaher Joukhadar (zjoukhadar@unimelb.edu.au)                     #
# ---------------------------------------------------------------              #
# Copyright 2022 - 2022, Melbourne Data Analytics Platform (MDAP)              #
################################################################################

from flax import linen as nn


class MyModel(nn.module):
    embd_dim: int
    patch_size: int
    dropout_prob: float
    num_classes: int

    def setup(self):
        self.input_layer = nn.Dense(self.embd_dim)
        self.dropout = nn.Dropout(self.dropout_prob)
        self.mlp_head = nn.Sequential([nn.LayerNorm(), nn.Dense(self.num_classes)])

    def __call__(self, x, train=True):
        inp_x = self.img_to_patch(x, self.patch_size)
        B, T, _ = x.shape

        out = self.input_layer(x)
        out = self.dropout(x, deterministic=not train)

        out = self.mlp_head(out)
        return out

    def img_to_patch(self, x, patch_size, flatten_channels=True):
        """
        Inputs:
            x - torch.Tensor representing the image of shape [B, H, W, C]
            patch_size - Number of pixels per dimension of the patches (integer)
            flatten_channels - If True, the patches will be returned in a flattened format
                            as a feature vector instead of a image grid.
        """
        B, H, W, C = x.shape
        x = x.reshape(B, H // patch_size, patch_size, W // patch_size, patch_size, C)
        x = x.transpose(0, 1, 3, 2, 4, 5)  # [B, H', W', p_H, p_W, C]
        x = x.reshape(B, -1, *x.shape[3:])  # [B, H'*W', p_H, p_W, C]
        if flatten_channels:
            x = x.reshape(B, x.shape[1], -1)  # [B, H'*W', p_H*p_W*C]
        return x
