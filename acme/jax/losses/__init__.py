# Copyright 2018 DeepMind Technologies Limited. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Common loss functions."""

from acme.jax.losses.impala import impala_loss
from acme.jax.losses.mpo import MPO
from acme.jax.losses.mpo import MPOParams
from acme.jax.losses.mpo import MPOStats
from acme.jax.losses.wpo import WPO
from acme.jax.losses.wpo import WPOParams
from acme.jax.losses.wpo import WPOStats
