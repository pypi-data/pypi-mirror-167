#!/usr/bin/env python
# ******************************************************************************
# Copyright 2022 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
from copy import copy
import tensorflow as tf


from ..debugging import assert_equal


@tf.function
@tf.custom_gradient
def round_through(x):
    rounded = tf.math.round(x)
    def grad(upstream):
        return upstream
    return rounded, grad


@tf.function
@tf.custom_gradient
def floor_through(x):
    floored = tf.math.floor(x)
    def grad(upstream):
        return upstream
    return floored, grad


@tf.function
@tf.custom_gradient
def ceil_through(x):
    ceiled = tf.math.ceil(x)
    def grad(upstream):
        return upstream
    return ceiled, grad


class QTensor(tf.experimental.ExtensionType):
    """Abstract class to exchange quantized tensors between layers

    The QTensor values are actually stored as integer, but it provides a
    conversion method to project these values into a float representation.

    The value_bits parameter sets the maximum integer values that can be stored:
        int_max = 2^bits - 1.

    When a QTensor is created, its values are clipped to [-int_max, int_max].
    """
    values: tf.Tensor = 1.0
    value_bits: int = 7
    shape: tf.TensorShape  # Required to convert to a KerasTensor

    @property
    def per_tensor(self):
        """Returns if QTensor is quantized per-tensor

        Returns:
            bool: True if QTensor is quantized per-tensor or False on per-axis case.
        """
        raise NotImplemented

    def to_float(self):
        """Returns a float representation of the QTensor

        Returns:
            :obj:`tensorflow.Tensor`: the float representation.
        """
        raise NotImplementedError

    def clone(self):
        """Returns a copy of the QTensor

        Returns:
            :obj:`QTensor`: the copy.
        """
        return copy(self)

    def __str__(self):
        x_float = self.to_float()
        return f"QTensor: {x_float}"

    @staticmethod
    def int_max(value_bits):
        return 2 ** value_bits - 1

    @staticmethod
    def clamp(values, value_bits):
        int_max = QTensor.int_max(value_bits)
        return tf.clip_by_value(values, -int_max, int_max)

    def assert_per_tensor(self):
        """Asserts that a QTensor is quantized per-tensor"""
        name = self.__class__.__name__ if not hasattr(self.values, "name") else self.values.name
        assert_equal(self.per_tensor, True, message=f"{name} is not per-tensor.")
