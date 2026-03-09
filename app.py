from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from screens import RootController

    

class TarotApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.accent_palette = "BlueGray"
        rc = RootController()
        return rc

    


if __name__ == "__main__":
    ta = TarotApp()
    ta.run()