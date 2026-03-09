from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import StringProperty, BooleanProperty


class HomeScreen(MDScreen):
    def get_primary(self):
        return self.app.theme_cls.primary_color
    
    @property
    def app(self):
        return MDApp.get_running_app()


class TarotScreen(MDScreen):
    pass

