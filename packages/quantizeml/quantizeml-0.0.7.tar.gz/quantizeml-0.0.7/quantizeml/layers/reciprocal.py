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
import keras
import tensorflow as tf

from ..tensors import ceil_through, FixedPoint, MAX_BUFFER_BITWIDTH
from .layers import deserialize_quant_object, Calibrable, CalibrableVariable


__all__ = ["Reciprocal", "QuantizedReciprocal"]


@tf.keras.utils.register_keras_serializable()
class Reciprocal(keras.layers.Layer):
    """Layer that computes the reciprocal of the input.
    """

    def call(self, inputs, training=False):
        return tf.math.reciprocal(inputs)


@tf.keras.utils.register_keras_serializable()
class QuantizedReciprocal(Calibrable, Reciprocal):
    """Piece-wise approximation of y = 1/x.

    The approximation works on values in the range [1, 2).
    To go into that range, we shift the input to put the leftmost bit (MSB) to
    1 and change the frac_bits so that there is only one int bit.
    Once that is done the approximation is as follows:

    y' = 1.59375 - 0.625 * x if x < 1.5
    y' = 1.125 - 0.3125 * x  if x >= 1.5

    Note that this can be performed in hardware this way:

    y' = 51 * 2^-5 - x * (2^-1 + 2^-3) if x < 1.5
    y' = 36 * 2^-5 - x * (2^-2 + 2^-4) if x >= 1.5

    Implementation inspired by:

    Cardarilli, G.C., Di Nunzio, L., Fazzolari, R. et al.
    A pseudo-softmax function for hardware-based high speed image classification.
    Sci Rep 11, 15307 (2021). https://doi.org/10.1038/s41598-021-94691-7

    Args:
        quant_config (dict, optional): the quantization configuration. Defaults to {}.

    """

    def __init__(self, *args, quant_config={}, **kwargs):
        super().__init__(*args, **kwargs)
        self.quant_config = quant_config
        self.buffer_bitwidth = quant_config.get("buffer_bitwidth", MAX_BUFFER_BITWIDTH) - 1
        self.out_quantizer = deserialize_quant_object(quant_config, "output_quantizer", False)

        # All constants are in the range |x| < 2. We only need 1 bit for the int part
        # and remove the sign bit.
        value_bits = self.buffer_bitwidth
        frac_bits = value_bits - 1
        self._K_1_125 = FixedPoint.quantize(1.125, frac_bits, value_bits)
        self._K_0_3125 = FixedPoint.quantize(-0.3125, frac_bits, value_bits)
        self._K_1_59375 = FixedPoint.quantize(1.59375, frac_bits, value_bits)
        self._K_0_625 = FixedPoint.quantize(-0.625, frac_bits, value_bits)
        # The limit is to choose the PWL function is 1.5 (= 3 * 2^-1), that only containts
        # 1 bit in int part
        self._limit_1_5 = FixedPoint.quantize(1.5, frac_bits, value_bits)

        # We need to store the input frac bits to reproduce the reciprocal on hardware.
        # Therefore, we save them regardless of whether they are in calibration mode or not
        self.input_frac_bits = CalibrableVariable()
        self.input_frac_bits.calibration = True

    def _reciprocal_x_ge_1_5_values(self, x):
        """Implements reciprocal approximation when x in [1.5, 2.0), following the equation:

        1/x = 1.125 - 0.3125 * x

        Args:
            x (:obj:`FixedPoint`): the value to compute its reciprocal.

        Returns:
            :obj:`FixedPoint`: the reciprocal result.
        """
        x = x * self._K_0_3125
        x_reciprocal = x + self._K_1_125
        return x_reciprocal.values

    def _reciprocal_x_lt_1_5_values(self, x):
        """Implements reciprocal approximation when x in [1.0, 1.5), following the equation:

        1/x = 1.59375 - 0.625 * x

        Args:
            x (:obj:`FixedPoint`): the value to compute its reciprocal.

        Returns:
            :obj:`FixedPoint`: the reciprocal result.
        """
        x = x * self._K_0_625
        x_reciprocal = x + self._K_1_59375
        return x_reciprocal.values

    def call(self, inputs, training=False):
        if not isinstance(inputs, FixedPoint):
            raise TypeError("QuantizedReciprocal only accepts FixedPoint inputs. "
                            f"Receives '{type(inputs)}' as inputs.")

        # Promote and get properties of FixedPoint
        inputs = inputs.promote(self.buffer_bitwidth)
        x_values = inputs.values
        x_frac_bits = inputs.frac_bits
        x_value_bits = inputs.value_bits

        # Store input frac_bits
        self.input_frac_bits(x_frac_bits)

        # Evaluate element-wise the number of bits used in x binary representation.
        # This operation can be done in hardware by counting leading zeros.
        used_bits = ceil_through(tf.experimental.numpy.log2(x_values))

        # The PWL function works in the range [1, 2).
        #
        # To project x into that range, we first align it element-wise to make sure
        # all items binary representation leftmost-bit are at one.
        #
        # x' = x << (x_value_bits - used_bits)
        #
        # which means:
        #
        # x'.values = x.values * 2 ^ (x.value_bits - used_bits)
        # x'.frac_bits = x_frac_bits + (x.value_bits - used_bits)
        #
        # Now, if we define y as the number with the same values as x' but (x.value_bits - 1)
        # fractional bits, it is guaranteed it is in the interval [1, 2).
        #
        # y.values = x'.values = x.values * 2 ^ (x.value_bits - used_bits)
        # y.frac_bits = x.value_bits - 1
        #
        y_values = inputs.mul_pow_2(x_value_bits - used_bits).values
        y_frac_bits = x_value_bits - 1
        y = FixedPoint(y_values, y_frac_bits, x_value_bits)

        # Estimate output values using one of the PWL functions
        reciprocal_y_values = tf.where(y >= self._limit_1_5,
                                       self._reciprocal_x_ge_1_5_values(y),
                                       self._reciprocal_x_lt_1_5_values(y))
        reciprocal_y = FixedPoint(reciprocal_y_values, y_frac_bits, x_value_bits)

        # Since we defined previously
        #
        # y.values = x.values * 2 ^ (x.value_bits - used_bits)
        # y.frac_bits = x.value_bits - 1
        #
        # We can express y as:
        #
        # y = y.values * 2 ^ (1 - x.value_bits)
        # y = x.values * 2 ^ (x.value_bits - used_bits) * 2 ^ (1 - x.value_bits)
        # y = x.values * 2 ^ (1 - used_bits)
        #
        # or x.values = y * 2 ^ (used_bits - 1)
        #
        # We can now express x as:
        # x = x.values * 2 (-x.frac_bits)
        # x = y * 2 ^(used_bits - 1 - x.frac_bits)
        #
        # and:
        #
        # 1/x = 1/y * 2^(x.frac_bits - used_bits + 1)
        #
        outputs = reciprocal_y.mul_pow_2(x_frac_bits - used_bits + 1)

        # Finally, passes result through output_quantizer
        if self.out_quantizer is not None:
            outputs = self.out_quantizer(outputs)
        return outputs

    def get_config(self):
        config = super().get_config()
        config["quant_config"] = self.quant_config
        return config
