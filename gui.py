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

from kivy.core.window import Window 
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

class MainFrame(FloatLayout):
    def __init__(self, **kwargs):
        super(MainFrame, self).__init__(**kwargs)
        Window.size = (1280, 720)
