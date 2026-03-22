import threading
from gen import generate_celtic_cross, generate_yes_no
from kivymd.app import MDApp
from kivy.animation import Animation
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


    def ask_pressed(self, instance=None):
        self.current_status.text = "Asking the void.."
        self.start_label_glow()
        if self.app.rc.has_api_key:
            akey = self.app.rc.api_key
            inq = self.app.rc.current_inquiry
            threading.Thread(target=self.generate_request, args=(akey, inq, "celtic")). start()
    

    def ask_yn(self, instance=None):
        self.current_status.text = "Asking the void.."
        self.start_label_glow()
        if self.app.rc.has_api_key:
            akey = self.app.rc.api_key
            inq = self.app.rc.current_inquiry
            threading.Thread(target=self.generate_request, args=(akey, inq, "yn")). start()
        

    def generate_request(self, akey, inq, spread):
        if spread == "celtic":
            response = generate_celtic_cross(akey,inq)
            try:
                Clock.schedule_once(lambda dt: self.update_ui(response, "The oracle has spoken.."))
            except Exception as e:
                ee = e
                Clock.schedule_once(lambda dt: self.update_ui(f"ERROR:{ee}", "Its fuzzy.."))
            
        if spread == "yn":
            response = generate_yes_no(akey,inq)
            try:
                Clock.schedule_once(lambda dt: self.update_ui(response, "The oracle has spoken.."))
            except Exception as e:
                ee = e
                Clock.schedule_once(lambda dt: self.update_ui(f"ERROR:{ee}", "Its fuzzy.."))    

        self.app.rc.current_reading = response 
            

    def update_ui(self, text = "...", status = "Empty"):
        self.res_label.text = text
        self.current_status.text = status
        try:
            Animation.stop(self.current_status,"text_color")
        except Exception as e:
            print(f"ERROR:\n{e}")
            Animation.cancel_all(self.current_status)


    def start_label_glow(self):
        glow1 = Animation(text_color=(0.25, 0.11, 0.40, 1), duration=3)
        glow2 = Animation(text_color=(0.10, 0.03, 0.20, 1), duration=2)
        anim = glow1 + glow2
        anim.repeat = True
        anim.start(self.current_status)
        

    @property
    def app(self):
        return MDApp.get_running_app()