from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty


class ReadingScreen(MDScreen):
    res_label = ObjectProperty()

    @property
    def app(self):
        return MDApp().get_running_app()