# Copyright (c) 2024 Intel Corporation
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from nncf.experimental.tensor.tensor import Tensor
from tests.post_training.test_templates.test_calculate_quantizer_parameters import TemplateTestFQParams


class TestFQParams(TemplateTestFQParams):
    def to_nncf_tensor(self, t):
        return Tensor(t)
