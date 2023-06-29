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
import GPUtil as gpu_info

def get_nvidia_infos(gpus):
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = gpu.load*100
        gpu_f_memory = gpu.memoryFree
        gpu_u_memory = gpu.memoryUsed
        gpu_t_memory = gpu.memoryTotal
        gpu_temp = gpu.temperature
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id,
            gpu_name,
            gpu_load,
            gpu_f_memory,
            gpu_u_memory,
            gpu_t_memory,
            gpu_temp,
            gpu_uuid
        ))
    return list_gpus