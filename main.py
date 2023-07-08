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

VER_MAJOR = '2023.07'
VER_MINOR = '35'
REVISION = 'Alpha'
VERSION_INFO = (VER_MAJOR, VER_MINOR, REVISION)
VERSION = '.'.join(str(c) for c in VERSION_INFO)
TITLE_WINDOW = f'System Monitoring'

import kivy
kivy.require('2.2.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

import functions, webbrowser, pyamdgpuinfo, psutil
import amd as AMD
import nvidia as NVIDIA
import system as SYSTEM

from kivy.config import Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')

class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

class MonitoringScreen(Screen):
    def __init__(self, **kwargs):
        super(MonitoringScreen, self).__init__(**kwargs)
        self.GPU = AMD.gpu(pyamdgpuinfo.get_gpu(0))
        self.SYS = SYSTEM.system()
        self.CPU = SYSTEM.cpu()
        self.NET = SYSTEM.network()
        Clock.schedule_interval(self.callback, 1)
        Clock.schedule_once(self.initCallback)
        
    def on_stop(self):
        Clock.unschedule(self.callback)
        
    def on_start(self):
        Clock.schedule_interval(self.callback, 1)
        
    def callback(self, dt):
    
        setattr(self, 'GPU', AMD.gpu(pyamdgpuinfo.get_gpu(0)))
        setattr(self, 'NET', SYSTEM.network())
        self.refreshScreen()
    
    def initCallback(self, dt):
        self.SYS.initCallback(self.ids)
        self.CPU.initCallback(self.ids)
            
    def refreshScreen(self):
        
        self.GPU.update(self.ids)
        self.NET.update(self.ids)
        
class OptionsScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class SystemMonitoring(App):
    
    def build(self):

        self.TITLE = TITLE_WINDOW
        self.VERSION = VERSION
        try:
            AMD.gpu(pyamdgpuinfo.get_gpu(0))
        except Exception as e:
            print(f'{e} || No AMD GPU found')
            raise SystemExit()
        
        return MainWindow()
    
    def hyperLink(self):
        webbrowser.open('https://www.gnu.org/licenses/gpl-3.0.html')
            
if __name__ == '__main__':
    SystemMonitoring().run()