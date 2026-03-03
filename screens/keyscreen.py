import os
import random
import threading
import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput



class KeyScreen(Screen):
    def on_pre_enter(self):
        self.keyfield = self.ids.keyfield
        if not os.path.exists(".key.key"):
            with open(".key.key","w") as f:
                f.close()

    def on_enter(self):
        self.update_field()

    def update_field(self):
        if self.check_key():
            self.keyfield.text = self.get_key()
    
    def check_key(self):
        print("check_key()")
        try:
            if os.path.exists(".key.key"):
                try:
                    with open(".key.key","r") as f:
                        contents = f.read()
                except Exception as e:
                    print(e)
                    return False
                if contents == "":
                    return False
                return True
            else:
                return False
        except Exception as e:
            print(e)
    
    def save_key(self):
        apikey = self.keyfield.text
        with open(".key.key","w") as f:
            f.write(apikey)
        self.update_field()
        self.manager.current = "input"

    def get_key(self):
            print("get_key()")
            try:
                if self.check_key():
                    with open(".key.key","r") as f:
                        akey = f.read()
                    return akey
            except Exception as e:
                print(e)

    def reset_key(self):
        if self.check_key():
            with open(".key.key","w") as f:
                f.write("")
                f.close()
            self.update_field()