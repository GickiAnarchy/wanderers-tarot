import json
from socketserver import DatagramRequestHandler
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
        self.cards = TarotCards()
        self.api_key = None
        self.current_inquiry = None
        self.current_reading = None
        self.current_spread = "Celtic Cross"


    def goto(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.title = screen_name.replace("_"," ").title()
        
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")


    def ask_question(self):
        if self.current_spread == "Celtic Cross":
            self.celtic_cross_spread()
            


    def celtic_cross_spread(self):
        response = generate_celtic_cross(self.api_key, self.current_inquiry)
        rs = self.screen_manager.get_screen("reading")
        rs.res_label.text = response
        self.screen_manager.current = "reading"
            

    @property
    def app(self):
        return MDApp().get_running_app()