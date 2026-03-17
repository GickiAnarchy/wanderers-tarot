import json
from datetime import datetime
import threading

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from models import TarotCards
from gen import generate_celtic_cross
from kivymd.uix.toolbar import MDTopAppBar



class RootController(MDBoxLayout):

    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.cards = TarotCards()
        self.api_key = None
        self.current_inquiry = None
        self.current_reading = None
        self.current_spread = "Celtic Cross"

        Clock.schedule_once(self.check_key, 1)

  
    def check_key(self, dt):
        settings_screen = self.screen_manager.get_screen("settings")
        if settings_screen.has_api_key:
            self.goto("home")
        else:
            print("Need API Key")
            self.goto("settings")


    def goto(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.title = screen_name.replace("_"," ").title()
        
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")


    def ask_question(self):
        rs = self.screen_manager.get_screen("reading")
        rs.ask_pressed()
        self.screen_manager.current = "reading"


    def save_reading(self):
        if self.current_reading is None:
            return
        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        data = {
            "timestamp": timestamp,
            "inquiry": self.current_inquiry,
            "spread": self.current_spread,
            "reading": self.current_reading
        }
        history = self.load_history()
        history.append(data)
        try:
            with open("history.json", "w") as f:
                json.dump(history, f, indent=4)
            print("reading saved")
        except Exception as e:
            print(f"Error saving history: {e}")


    def load_history(self):
        try:
            with open("history.json", "r") as f:
                history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
            print(f"Error loading history: {e}")
            history = []
        return history


    @property
    def has_api_key(self):
        return self.screen_manager.get_screen("settings").has_api_key


    @property
    def app(self):
        return MDApp().get_running_app()