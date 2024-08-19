
import datetime

from kivy.config import Config
Config.set("kivy","keyboard mode","dock")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image, AsyncImage
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

from src.geminiRequest import pastPresentFuture, celticCross, treeOfLife, simpleReply
from src.tarot import TarotDeck, Reading
from src.serialize import getRandomPNG



class WanderersBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reading_btn = ObjectProperty(None)
        self.search_btn = ObjectProperty(None)
        self.question_box = ObjectProperty(None)

    def searchCards(self, instance):
        pass

    def readTarot(self, instance):
        if self.question_box.text in [None, ""]:
            return
        reading = Reading()
        reading.drawCards(10)
        ai_reading = celticCross(reading)
        return

class WTApp(App):
    def build(self):
        self.box = BoxLayout()
        self.cardimg = Image()
        self.wbox = WanderersBox()
        self.wbox.pos_hint = {'center_x': 0.5}
        self.update()
        return self.box


    def update(self):
        ran_img = getRandomPNG("img/")
        self.cardimg.source = ran_img
        self.box.add_widget(self.cardimg)
        self.box.add_widget(self.wbox)

"""

        #_#

"""
def getTime(self):
    if self.formatted_date == None:
        now = datetime.datetime.now()
        self.formatted_date = now.strftime("%m/%d/%Y %H:%M")
    return self.formatted_date


if __name__ == "__main__":
    WTApp().run()

