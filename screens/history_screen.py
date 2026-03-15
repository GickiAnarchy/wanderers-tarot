import os
import json

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class HistoryScreen(MDScreen):
    HISTORY_FILE = "history.json"
    
    
    def get_history(self):
        if os.path.exists(self.HISTORY_FILE):
            with open(self.HISTORY_FILE, "r") as f:
                data = json.load(f)
            return data


    def save_history(self, newdata):
        if newdata is None:
            print("newdata is None. Nothing to add to history")
            return
        with open(self.HISTORY_FILE, "w") as f:
            json.dump(newdata, f, indent=4)
            