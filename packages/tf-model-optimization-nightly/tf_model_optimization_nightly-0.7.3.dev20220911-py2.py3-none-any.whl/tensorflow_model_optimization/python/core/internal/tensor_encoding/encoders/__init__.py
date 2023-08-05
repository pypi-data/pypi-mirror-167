# Copyright 2019, The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A collection of common encoders."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_model_optimization.python.core.internal.tensor_encoding.encoders.common_encoders import as_gather_encoder
from tensorflow_model_optimization.python.core.internal.tensor_encoding.encoders.common_encoders import as_simple_encoder
from tensorflow_model_optimization.python.core.internal.tensor_encoding.encoders.common_encoders import hadamard_quantization
from tensorflow_model_optimization.python.core.internal.tensor_encoding.encoders.common_encoders import identity
from tensorflow_model_optimization.python.core.internal.tensor_encoding.encoders.common_encoders import uniform_quantization
