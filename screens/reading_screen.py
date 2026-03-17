import threading
from gen import generate_celtic_cross
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.scrollview import MDScrollView


class ReadingScreen(MDScreen):
    res_label = ObjectProperty()
    current_status = ObjectProperty()
    
    
    def ok_pressed(self, instance=None):
        self.app.rc.save_reading()
        self.manager.current = "home"


    def ask_pressed(self, instance=None):#self.current_status.text = "Asking the void"
        if self.app.rc.has_api_key:
            akey = self.app.rc.api_key
            inq = self.app.rc.current_inquiry
            threading.Thread(target=self.generate_request, args=(akey, inq)). start()
        

    def generate_request(self, akey, inq):
        response = generate_celtic_cross(akey,inq)
        try:
            Clock.schedule_once(lambda dt: self.update_ui(response, "The oracle has spoken.."))
        except Exception as e:
            ee = e
            Clock.schedule_once(lambda dt: self.update_ui(f"ERROR:{ee}", "Its fuzzy.."))
            

    def update_ui(self, text = "...", status = "Empty"):
        self.res_label.text = text
        self.current_status.text = status   
    

    @property
    def app(self):
        return MDApp.get_running_app()