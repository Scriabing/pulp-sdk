#
# Copyright (C) 2018 ETH Zurich, University of Bologna and
# GreenWaves Technologies
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
#

from generators.v1.comp_gen import *
import collections
import json_tools as js



def gen_config(name, system_config, system, device_config, usecases=[]):

  itf = device_config.get_str('interface')
  cs = device_config.get_str('cs')

  system.system_tree.board.add_component(name, Tb_Component(
    config=device_config.get('config'),
    properties=OrderedDict([
      ('name', name)
    ])
  ))

  gpio_ready = device_config.get_child_str('gpio_ready')
  system.system_tree.board.chip.set(gpio_ready, system.system_tree.board.dpi.new_itf(gpio_ready))
  system.system_tree.board.chip.set(gpio_ready, system.system_tree.board.get(name).new_itf('gpio_ready'))

  system.system_tree.board.chip.set(itf + '_cs' + str(cs) + '_data', system.system_tree.board.dpi.new_itf(itf + '_cs' + str(cs) + '_data'))
  system.system_tree.board.chip.set(itf + '_cs' + str(cs), system.system_tree.board.dpi.new_itf(itf + '_cs' + str(cs)))

  system.system_tree.board.chip.set(itf + '_cs' + str(cs) + '_data', system.system_tree.board.get(name).input)
