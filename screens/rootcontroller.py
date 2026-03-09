from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screenmanager import MDScreenManager
from screens.screens import TarotScreen
from screens.settings_screen import SettingsScreen
from .home_screen import HomeScreen 

class RootController(MDBoxLayout):

    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()

    def goto(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.title = screen_name.replace("_"," ").title()
        
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")
    
    def get_api_key(self):
        settings_screen = self.screen_manager.get_screen("Settings")
        akey = settings_screen.get_api_key()
        print(akey)
        return akey
    
    def save_api_key(self,instance):
        self.screen_manager.get_screen("settings").save_api_key(self.screen_manager.get_screen("settings").api_key)