from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty


class TarotScreen(MDScreen):
    inquiry = StringProperty(None)
    in_field = ObjectProperty(None)
    
    def ask_pressed(self, instance = None):
        if self.in_field.text is "" or self.in_field.text is None:
            return
        self.inquiry = self.in_field.text
    
    

    @property
    def app(self):
        return MDApp.get_running_app()