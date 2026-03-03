## MAIN.PY

import os
import random
import threading
import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from gen import generate
from wtutils import get_image


class TarotApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(ReadingScreen(name='reading')),
        sm.add_widget(KeyScreen(name='key'))
        return sm
    

if __name__ == '__main__':
    TarotApp().run()
    
##