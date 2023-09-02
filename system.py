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
import psutil, re, stat, pyamdgpuinfo, platform
from subprocess import check_output as bashCMD

class system:
    def __init__(self):
        self.gpuName = pyamdgpuinfo.get_gpu(0).name
        self.osName = platform.system()
        self.kernel = platform.platform()
        self.swapUsed = f'{str(round(psutil.swap_memory().used / 1073741824, 1))} GB'
        self.swapTotal = f'{str(round(psutil.swap_memory().total / 1073741824, 1))} GB'
        self.swapLoad = f'{str(round(psutil.swap_memory().percent, 1))} %'
        self.memUsed = f'{str(round((psutil.virtual_memory().total - psutil.virtual_memory().available) / 1073741824, 1))} GB'
        self.memTotal = f'{round(psutil.virtual_memory().total / 1073741824, 1)} GB'
        self.memLoad = f'{str(psutil.virtual_memory().percent)} %'
        
    def initCallback(self, box):
        box.gpu_name.text = self.gpuName
        box.system_name.text = self.osName
        box.kernel.text =  re.sub("-with.*", "", self.kernel, 1)
        box.swap_total.text = self.swapTotal
        box.memory_total.text = self.memTotal
    
    def update(self, box):
        box.swap_used.text = self.swapUsed
        box.swap_load.text = self.swapLoad
        box.memory_used.text = self.memUsed
        box.memory_load.text = self.memLoad
    
class network:
    def __init__(self):
        self.dSent, self.sUnit = self.formatBytes(psutil.net_io_counters().bytes_sent)
        self.dRecv, self.rUnit = self.formatBytes(psutil.net_io_counters().bytes_recv)
        net_cards = psutil.net_if_stats()
        net_card_dict = {}

        for name, value in net_cards.items():
            net_card_dict[name] = value[0]

        active_net = 'None'

        for name, value in net_card_dict.items():
            if name != 'lo' and value:
                active_net = name

        net_card_pass = False
        if active_net != 'None':
            try:
                self.card = active_net
                self.ipv4Address = psutil.net_if_addrs()[active_net][0].address
                self.ipv6Address = psutil.net_if_addrs()[active_net][1].address
                self.speed = psutil.net_if_stats()[active_net].speed / 8
                self.duplex = psutil.net_if_stats()[active_net][1]
                if self.duplex == 1:
                    self.duplexType = 'Half Duplex'
                elif self.duplex == 2:
                    self.duplexType = 'Full Duplex'
                else:
                    self.duplexType = 'N/A'
                net_card_pass = True
            except Exception as e:
                print(e)
                raise SystemExit()
        else:
            self.card = active_net
            self.ipv4Address = 'N/A'
            self.ipv6Address = 'N/A'
            self.speed = 'N/A'
    
    def formatBytes(self, bytes):
        self.f_bytes = 0
        self.f_unit = ''
        if bytes < 1024:
            self.f_bytes = bytes
            self.f_unit = 'Byte(s)/s'
        elif bytes >= 1024 and bytes < 1048576:
            self.f_bytes = round(bytes / 1024, 2)
            self.f_unit = 'KB/s'
        elif bytes >= 1048576 and bytes < 1073741824:
            self.f_bytes = round(bytes / 1048576, 2)
            self.f_unit = 'MB/s'
        elif bytes > 1073741824:
            self.f_bytes = round(bytes / 1073741824, 2)
            self.f_unit = 'GB/s'
        return self.f_bytes, self.f_unit
    
    def netCounterCalc(self, bRecv, bSent):
        self.t_recv = (psutil.net_io_counters().bytes_recv - bRecv)
        self.t_sent = (psutil.net_io_counters().bytes_sent - bSent)
        return self.t_recv, self.t_sent
    
    def update(self, box):
        box.net_data_recv.text = f'{self.dRecv} {self.rUnit}'
        box.net_data_sent.text = f'{self.dSent} {self.sUnit}'
        box.net_card.text = self.card
        box.net_ipv4.text = self.ipv4Address
        box.net_ipv6.text = self.ipv6Address
        box.net_speed.text = f'{self.speed} MB/s'
        box.net_duplex.text = self.duplexType
        
class cpu:
    def __init__(self):
        self.load = f'{str(int(psutil.cpu_percent()))} %'
        self.clock = f'{str(round(psutil.cpu_freq()[0] / 1000, 2))} GHz'
        self.temp = f'{str(round(psutil.sensors_temperatures()["k10temp"][0][1], 1))} °C'
        self.l1Cache = bashCMD("lscpu | grep 'L1d' | sed 's/:/%/' | cut -d'%' -f2 | cut -d'(' -f1", shell = True).decode().replace(' ', '').strip()
        self.l2Cache = bashCMD("lscpu | grep 'L2' | sed 's/:/%/' | cut -d'%' -f2 | cut -d'(' -f1", shell = True).decode().replace(' ', '').strip()
        self.l3Cache = bashCMD("lscpu | grep 'L3' | sed 's/:/%/' | cut -d'%' -f2 | cut -d'(' -f1", shell = True).decode().replace(' ', '').strip()
        self.infos = bashCMD("cat /proc/cpuinfo", shell=True).decode().strip()
        for line in self.infos.split("\n"):
            if 'model name' in line:
                self.name = re.sub( ".*model name.*:", "", line,1)
                if 'Processor' in self.name:
                    self.name = re.sub(" Processor", "", self.name, 1)
    
    def initCallback(self, box):
        box.cpu_name.text = self.name
        box.cpu_l1_cache.text = self.l1Cache
        box.cpu_l2_cache.text = self.l2Cache
        box.cpu_l3_cache.text = self.l3Cache
        
    def update(self, box):
        box.cpu_clock.text = self.clock
        box.cpu_load.text = self.load
        box.cpu_temp.text = self.temp
