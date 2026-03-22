


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty, StringProperty, NumericProperty



class YesOrNoScreen(MDScreen):
    
    @property
    def app(self):
        return MDApp.get_running_app()