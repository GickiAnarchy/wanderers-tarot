import os
import json

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

#####
##  API Key Management
#####
    def save_api_key(self, apikey, instnance = None):
        if apikey is "" or apikey is None:
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
    
    def reset_api_key(self):
        self.api_key = ""
        if os.path.exists(KEYFILE):
            os.remove(KEYFILE)
    
