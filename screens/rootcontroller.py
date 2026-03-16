import json

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from models import TarotCards
from gen import generate
from kivymd.uix.toolbar import MDTopAppBar



class RootController(MDBoxLayout):

    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cards = TarotCards()


    def goto(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.title = screen_name.replace("_"," ").title()
        
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")


    @property
    def app(self):
        return MDApp.get_running_app()