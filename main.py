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
 # along with nvtop.  If not, see <http://www.gnu.org/licenses/>.

VER_MAJOR = '2023.06.1'
VER_MINOR = 'Alpha'
REVISION = '1'
VERSION_INFO = (VER_MAJOR, VER_MINOR, REVISION)
VERSION = '.'.join(str(c) for c in VERSION_INFO)
TITLE_WINDOW = f'Modpack Updater v{VERSION}'

from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')

import kivy
kivy.require('2.2.1')
from kivy.app import App

from kivy.core.window import Window 
from kivy.uix.floatlayout import FloatLayout

class MainFrame(FloatLayout):
    def __init__(self, **kwargs):
        super(MainFrame, self).__init__(**kwargs)

class SystemMonitoring(App):
    
    def build(self):
        self.title = TITLE_WINDOW
        self.VERSION = VERSION

if __name__ == '__main__':
    SystemMonitoring().run()