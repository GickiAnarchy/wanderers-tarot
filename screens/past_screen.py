

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty


class PastReading(MDScreen):
    past_inquiry = ObjectProperty()
    past_response = ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.past_reading = None


    def update_screen(self, pr):
        self.past_reading = pr
        try:
            inq = pr.get("inquiry","")
            ts = pr.get("timestamp")
            self.past_inquiry.text = f"{ts}\n{inq}"
            self.past_response.text = pr.get("reading","")
        except Exception as e:
            print(e)


    def on_leave(self):
        print("leaving past reading screen")
    
    
    def delete_reading(self, instance = None):
        self.app.rc.delete_history(self.past_reading)
        self.manager.current = "history"

    
    @property
    def app(self):
        return MDApp.get_running_app()