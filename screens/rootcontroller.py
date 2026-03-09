from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screenmanager import MDScreenManager
from screens.screens import HomeScreen,TarotScreen,SettingsScreen

class RootController(MDBoxLayout):

    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()

    def goto(self, screen_name):
        self.screen_manager.current = screen_name
        self.toolbar.title = screen_name.replace("_"," ").title()
        
        if self.nav_drawer:
            self.nav_drawer.set_state("closed")