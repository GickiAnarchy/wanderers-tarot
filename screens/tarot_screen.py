import threading
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty



class TarotScreen(MDScreen):
    inquiry = StringProperty(None)
    in_field = ObjectProperty(None)

    def ask_pressed(self, instance=None):
        if self.in_field.text:
            self.inquiry = self.in_field.text
            self.app.rc.ask_question()
    
    def on_inquiry(self, instance, value):
        print(f"current_inquiry is now {value}")
        self.app.rc.current_inquiry = self.inquiry
        self.in_field.text = ""
        

    @property
    def app(self):
        return MDApp.get_running_app()
