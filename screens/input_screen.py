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



class InputScreen(Screen):
    def submit(self, instance):
        kscreen = self.manager.get_screen('key')
        if not kscreen.check_key():
            self.manager.current = 'key'
            return
        cc = 10
        self.question = self.ids.user_q.text
        question = self.question
        if question.strip():
            self.read_celtic()

    def read_celtic(self,instance = None):
        reading_screen = self.manager.get_screen('reading')
        reading_screen.start_reading(self.question, 10)
        self.manager.current = 'reading'
    
    def read_basic(self,instance):
        reading_screen = self.manager.get_screen('reading')
        reading_screen.start_reading(self.question, 2)
        self.manager.current = 'reading'
    
    def get_tarot_image(self):
        return get_image()