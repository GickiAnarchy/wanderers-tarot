from kivy.uix.screenmanager import ScreenManager
import screens


class TarotScreenManager(ScreenManager):
    def set_up(self):
        self.add_widget(screens.InputScreen(), "input")
        self.add_widget(screens.ReadingScreen(), "reading")
        self.add_widget(screens.KeyScreen(), "key")
        

    def go_to_screen(self, screen):
        self.current = screen
