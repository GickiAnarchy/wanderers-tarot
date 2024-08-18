
import datetime

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


class WanderersBox(BoxLayout):
    def __init__(self):
        self.reading_btn = ObjectProperty(None)
        self.search_btn = ObjectProperty(None)
        self.question_box = ObjectProperty(None)

    def searchCards(self):
        pass

    def readTarot(self, question):
        reading = Reading()
        reading.drawCards(10)
        ai_reading = celticCross(reading)
        return 

class WTApp(App):
    def build(self):
        self.wbox = ObjectProperty(None)
        return self.wbox


"""

        #_#

"""
def getTime(self):
    if self.formatted_date == None:
        now = datetime.datetime.now()
        self.formatted_date = now.strftime("%m/%d/%Y %H:%M")
    return self.formatted_date




if __name__ == "__main__":
    q = WTApp()
    q.run()

