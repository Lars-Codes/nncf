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


import numpy as np
import pytest

from nncf.experimental.tensor import Tensor
from tests.common.experimental.test_statistic_collector import TemplateTestStatisticCollector


class TestOVStatisticCollector(TemplateTestStatisticCollector):
    def get_nncf_tensor(self, value: np.ndarray) -> Tensor:
        return Tensor(value)

    @pytest.mark.skip()
    def test_median_mad_stat_building(self):
        pass

    @pytest.mark.skip
    def test_percentile_max_stat_building(self):
        pass
