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
 
from locale import getlocale
from datetime import datetime
from json import load,dump
from psutil import net_io_counters

def getLang():
    # Determine langage
    loc, enc = getlocale()
    if loc == 'fr_FR':
        lang = 'fr'
    else:
        lang = 'en'
    ## Uncomment this line to force English trad. For dev purposes
    # lang = 'en'
    return lang

def crashLog(data):
    crashPath = 'crash'
    crashFile = 'crash.log'
    _data = f'{datetime.now().strftime("[%d/%m/%y][%H:%M:%S][ERROR]: ")}{datas}\n'
    
    if path.exists(crashPath) != True:
        mkdir(crashPath)
    with open(f'{crashPath}/{crashFile}', 'a') as f:
        f.write(_datas)
    sys.exit(f'An error as occured. See crash.log at {crashPath}/{crashFile} for more informations.')

def manipulateFile(file, mode, data=""):
    if mode == 'r':
        try:
            with open(file, 'r') as f:
                j = load(f)
                return j
        except Exception as e:
            crashLog(f'{e} : manipulateFile({file}, "r") call (functions.py)')
    elif mode == 'w':
        try:
            with open(file, 'w') as f:
                dump(data, f)
        except Exception as e:
            crashLog(f'{e} : manipulateFile({file}, "w") call (functions.py)')

def getGPUFansMode(path):
    locFile = manipulateFile('locales.json', 'r')
    sysLang = getLang()
    locales = locFile[sysLang]
    
    f = manipulateFile(path, 'r')
    try:
        if f == 2:
            return locales['o_auto']
        elif f == 1:
            return locales['o_custom']
        elif f == 0:
            return locales['o_deactivated']
    except Exception as e:
        crashLog(f'{e} : getGPUFansMode({path}) call (functions.py)')

def byteCalculation(bytes):
    f_bytes = 0
    f_unit = ''
    if bytes < 1024:
        f_bytes = bytes
        f_unit = 'byte'
    elif bytes >= 1024 and bytes < 1048576:
        f_bytes = round(bytes / 1024, 2)
        f_unit = 'kb'
    elif bytes >= 1048576 and bytes < 1073741824:
        f_bytes = round(bytes / 1048576, 2)
        f_unit = 'mb'
    elif bytes > 1073741824:
        f_bytes = round(bytes / 1073741824, 2)
        f_unit = 'gb'
    return f_bytes,f_unit

def netCountData():
    # Calculate Bytrate per second
    try:
        totalReceivedNow = net_io_counters().bytes_recv
        totalSendNow = net_io_counters().bytes_sent
        sleep(0.5)
        totalReceivedDelayed = net_io_counters().bytes_recv
        totalSendDelayed = net_io_counters().bytes_sent
        totalReceived = (totalReceivedDelayed - totalReceivedNow) * 2
        totalSend = (totalSendDelayed - totalSendNow) * 2
        return totalReceived,totalSend
    except Exception as e:
        crashLog(f'{e} : netCountData() call (functions.py)')

def getCPUName():
    command = 'cat /proc/cpuinfo'
    infos = subprocess.check_output(command, shell=True).decode().strip()
    try:
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub( ".*model name.*:", "", line,1)
    except Exception as e:
        crashLog(f'{e} : getCPUName() call (functions.py)')

def setFansSpeed(value, path):
    try:
        subprocess.check_output(f'echo "{value}" | sudo tee {path}', shell=True)
    except Exception as e:
        crashLog(f'{e} : setFansSpeed({value} call (path: {path})) (functions.py)')

def setGPUFansMode(value, path):
    try:
        subprocess.check_output(f'echo "{value}" | sudo tee {path}', shell=True)
    except Exception as e:
        crashLog(f'{e} : setFansMode({value}) call (functions.py)')

def getGPUTemp(path):
    try:
        temp = int(int(manipulateFile(path, 'r')) / 1000)
    except Exception as e:
        crashLog(f'{e} : getGPUTemp() call (functions.py)')
    return temp