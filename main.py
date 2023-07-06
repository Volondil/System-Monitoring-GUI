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
VER_MINOR = '32'
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

import functions, webbrowser

class MainWindow(FloatLayout):
    pass

class MonitoringScreen(Screen):
    pass

class OptionsScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class SystemMonitoring(App):
    
    def build(self):

        self.title = TITLE_WINDOW
        self.VERSION = VERSION
        return MainWindow()
    
    def hyperLink(self):
        webbrowser.open('https://www.gnu.org/licenses/gpl-3.0.html')
    
if __name__ == '__main__':
    SystemMonitoring().run()