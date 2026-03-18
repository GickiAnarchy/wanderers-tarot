from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from screens import RootController, ALL_SCREENS
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem



class TarotApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Amber"
        self.rc = RootController()
        for cls,name in ALL_SCREENS:
            self.rc.screen_manager.add_widget(cls(name = name))
            print(f"{name} added to screen manager")
        self.rc.screen_manager.current = "home"
        return self.rc


    def on_stop(self, **kwargs):
        super().on_stop(**kwargs)
        print("CLOSING APP")


    @property
    def root_manager(self):
        return self.rc


if __name__ == "__main__":
    ta = TarotApp()
    ta.run()