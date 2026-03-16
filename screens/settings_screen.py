import os
import json

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


KEYFILE = "keyfile.json"

class SettingsScreen(MDScreen):
    api_key = StringProperty(None)

    def on_enter(self):
        pass

#####
##  API Key Management
#####
    def save_api_key(self, apikey, instnance = None):
        if apikey == "" or apikey == None:
            return
        self.api_key = apikey
        with open(KEYFILE, "w") as f:
            json.dump({"api_key": self.api_key}, f)
    
    def get_api_key(self):
        if self.api_key is not None:
            return self.api_key
        if not os.path.exists(KEYFILE):
            return ""
        try:
            with open(KEYFILE, "r") as f:
                data = json.load(f)
            self.api_key = data.get("api_key", "")
        except json.JSONDecodeError:
            self.api_key = ""
        return self.api_key

    def on_api_key(self, instance, value):
        print("SettingsScreen.on_api_key()\n")
        print(f"{instance}\n{value}\n")
        self.app.rc.api_key =  self.api_key
        print("api_key saved in app.root.api_key")
        self.app.rc.goto("home")

    def reset_api_key(self):
        self.api_key = ""
        if os.path.exists(KEYFILE):
            os.remove(KEYFILE)
    
    @property
    def app(self):
        return MDApp.get_running_app()