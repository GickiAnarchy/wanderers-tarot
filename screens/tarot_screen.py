import threading
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from gen import generate, generate_celtic_cross


class TarotScreen(MDScreen):
    inquiry = StringProperty(None)
    in_field = ObjectProperty(None)

    @property
    def app(self):
        return MDApp.get_running_app()
