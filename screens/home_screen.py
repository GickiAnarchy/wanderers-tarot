from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.clock import Clock
from kivy.animation import Animation
from custom_widgets import SpinningLogo


class HomeScreen(MDScreen):
    logo = ObjectProperty()
    app_title = ObjectProperty()
    
    def on_pre_enter(self):
        pass

    def on_enter(self):
        Clock.schedule_once(self.start_label_glow,1)
        
    def start_label_glow(self,dt=None):
        glow1 = Animation(text_color=(0.25, 0.11, 0.40, 1), duration=2)
        glow2 = Animation(text_color=(0.13, 0.05, 0.25, 1), duration=2)
        glow3 = Animation(text_color=(0.05, 0.01, 0.33, 0.6), duration=2)
        glow4 = Animation(text_color=(0.18, 0.08, 0.38, 0.9), duration=2)
        anim = glow1 + glow2 + glow3 + glow4
        anim.repeat = True
        anim.start(self.app_title)
        self.logo.spin()
    
    def get_primary(self):
        return self.app.theme_cls.primary_color
    
    def get_cotd(self):
        cotd = self.app.root_manager.cotd()
        return f"Card Of The Day\n--------------------------------\n{cotd}"
    
    @property
    def app(self):
        return MDApp.get_running_app()