# Copyright (C) 2021-2023 Rabouteau Yoan <rabouteau.yoan@outlook.fr>
#
# This file is part of System Monitoring.
#
# System Monitoring is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# System Monitoring is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software. If not, see <http://www.gnu.org/licenses/>.

import psutil, datetime, json
from kivy.clock import Clock
import pyamdgpuinfo

class gpu:
    def __init__(self, gpu):
        self.name = gpu.name
        self.load = str(int(gpu.query_load() * 100))
        self.memUsage = str(round(gpu.query_vram_usage() / 1073741824, 1))
        self.clock = str(int(round(gpu.query_sclk() / 1000000, 2)))
        self.gtt = str(round(gpu.query_gtt_usage() / 1073741824, 1))
        self.power = str(gpu.query_power())
        self.voltage = str(round(gpu.query_graphics_voltage(), 3))
        self.fansMode = getFansMode('/sys/class/hwmon/hwmon3/pwm1_enable') # Using fix path, have to add function for determine real path
        self.maxClock = str(int(gpu.query_max_clocks()['sclk_max'] / 1000000))
        self.memMax = str(round(gpu.memory_info['vram_size'] / 1073741824, 1))
        self.memClockMax = str(int(gpu.query_max_clocks()['mclk_max'] / 1000000))
        self.temp = str(int(psutil.sensors_temperatures()["amdgpu"][0][1]))
        self.chipTemp = str(int(psutil.sensors_temperatures()["amdgpu"][1][1]))
        self.fansSpeed = str(psutil.sensors_fans()["amdgpu"][0][1])
        self.memTemp = str(int(psutil.sensors_temperatures()["amdgpu"][2][1]))
        
    def update(self, box):
        #self.name have to add to system bos (sys_box)
        box.load.text = self.load + ' %'
        box.mem_usage.text = self.memUsage + ' GB'
        box.clock.text = self.clock + ' Mz'
        box.gtt.text = self.gtt + ' GB'
        #box.power.text = self.power
        #box.voltage.text = self.voltage
        box.fans_mode.text = self.fansMode
        box.max_clock.text = self.maxClock + ' MHz'
        box.mem_max.text = self.memMax + ' GB'
        box.mem_clock_max.text = self.memClockMax + ' MHz'
        box.temp.text = self.temp + ' °C'
        box.chip_temp.text = self.chipTemp + ' °C'
        box.fans_speed.text = self.fansSpeed + ' Tr/m'
        box.mem_temp.text = self.memTemp + ' °C'
        
def getFansMode(path):
    f = file_operate(path, 'r')
    if f == 2:
        return 'Automatique'
    elif f == 1:
        return 'Personnalisé'
    elif f == 0:
        return 'Désactivé'
    else:
        return 'ERROR'
        
def file_operate(file, mode, data=""):
    if mode == 'r':
        try:
            with open(file, 'r') as f:
                j = json.load(f)
                return j
        except Exception as e:
            print(f'{e} : file_operate({file}) call (with open ({file}, "r")) (misc.py)')
    elif mode == 'w':
        try:
            with open(file, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f'{e} : file_operate({file}) call (with open ({file}, "w")) (misc.py)')