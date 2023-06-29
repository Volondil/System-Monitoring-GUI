 # Copyright (C) 2021-2022 Rabouteau Yoan <rabouteau.yoan@outlook.fr>
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
 # along with nvtop.  If not, see <http://www.gnu.org/licenses/>.
import pyamdgpuinfo as gpuInfo
import psutil

class infos:
    def __init__(self, gpu):
        #gpu = gpuInfo.get_gpu(gpu_id)
        self.name = gpu.name
        self.load = int(gpu.query_load() * 100)
        self.memoryUsage = round(gpu.query_vram_usage() / 1073741824, 1)
        self.clock = int(round(gpu.query_sclk() / 1000000, 2))
        self.power = gpu.query_power()
        self.voltage = round(gpu.query_graphics_voltage(), 3)
        self.fansMode = get_gpu_fans_mode(hwmon_path + '/pwm1_enable')
        self.maxClocks = int(gpu.query_max_clocks()['sclk_max'] / 1000000)
        self.maxMemory = round(gpu.memory_info['vram_size'] / 1073741824, 1)
        self.maxMemoryClock = int(gpu.query_max_clocks()['mclk_max'] / 1000000)
        self.edgeTemp = int(psutil.sensors_temperatures()["amdgpu"][0][1])
        self.junctionTemp = int(psutil.sensors_temperatures()["amdgpu"][1][1])
        self.fansSpeed = psutil.sensors_fans()["amdgpu"][0][1]
        self.memoryTemp = int(psutil.sensors_temperatures()["amdgpu"][2][1])

