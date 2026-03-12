from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from gen import generate


class TarotScreen(MDScreen):
    inquiry = StringProperty(None)
    in_field = ObjectProperty(None)

    def ask_pressed(self, instance = None):
        if self.in_field.text:
            self.app.root_manager.send_inquiry(self.in_field.text, 10)

    @property
    def app(self):
        return MDApp.get_running_app()
