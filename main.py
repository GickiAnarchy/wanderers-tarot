## MAIN.PY


__version__ = "1.0.0"

import os
import random
import threading
import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from gen import generate
from wtutils import get_image





class InputScreen(Screen):
    def submit(self, instance):
        kscreen = self.manager.get_screen('key')
        if not kscreen.check_key():
            self.manager.current = 'key'
            return
        cc = 10
        question = self.ids.user_q.text
        if question.strip():
            if "DEBUG" in question:
                question = question.replace("DEBUG","")
                cc = 2
            reading_screen = self.manager.get_screen('reading')
            reading_screen.start_reading(question, cc)
            self.manager.current = 'reading'

    def read_celtic(self,instance):
        pass
    
    def read_basic(self,instance):
        pass
    
    def get_tarot_image(self):
        return get_image()




class ReadingScreen(Screen):
    def start_reading(self, question, cc=10):
        self.ids.status.text = "Consulting the stars via REST API..."
        threading.Thread(target=self.generate_reading, args=(question, cc)).start()

    def generate_reading(self, question, card_count=10):
        try:
            cards = Cards()
            drawn_cards = random.sample(cards.card_names, card_count)
            card_str = cards.get_desc(drawn_cards)
            drawn = ", ".join(drawn_cards)
            
            # Logic for instructions based on card count
            instruct = "Determine an insightful response for the seekers inquiry with the cards drawn."
            if card_count == 2:
                instruct = "Answer with a simple one-word response i.e. 'Yes', 'No', or 'Maybe'."
            
            prompt = f"Seekers Question: '{question}'. Cards Drawn: {card_str}. Instructions: {instruct}"
            
            # Call our REST-based generate function
            response = generate(prompt)
             
            final_text = f"The Cards: {drawn}\n\n{response}"
            Clock.schedule_once(lambda dt: self.update_ui(final_text, "The Oracle has spoken."))
            
        except Exception as e:
            error_str = str(e)
            Clock.schedule_once(lambda dt: self.update_ui(f"The connection was lost: {error_str}", "Error"))

    def update_ui(self, text, status):
        self.ids.reading_label.text = text
        self.ids.status.text = status

    def go_back(self, instance):
        self.manager.current = 'input'
        self.ids.reading_label.text = ""


class KeyScreen(Screen):
    def on_pre_enter(self):
        self.keyfield = self.ids.keyfield
        if os.path.exists(".key.key"):
            with open(".key.key","w") as f:
                f.close()

    def on_enter(self):
        self.update_field()

    def update_field(self):
        if self.check_key():
            self.keyfield.text = self.get_key()
    
    def check_key(self):
        print("check_key()")
        try:
            if os.path.exists(".key.key"):
                try:
                    with open(".key.key","r") as f:
                        contents = f.read()
                except Exception as e:
                    print(e)
                    return False
                if contents == "":
                    return False
                return True
            else:
                return False
        except Exception as e:
            print(e)
    
    def save_key(self):
        apikey = self.keyfield.text
        with open(".key.key","w") as f:
            f.write(apikey)
        self.update_field()
        self.manager.current = "input"
        
    
    def get_key(self):
            print("get_key()")
            try:
                if self.check_key():
                    with open(".key.key","r") as f:
                        akey = f.read()
                    return akey
            except Exception as e:
                print(e)

    def reset_key(self):
        if self.check_key():
            with open(".key.key","w") as f:
                f.write("")
                f.close()
            self.update_field()


class Cards:
    def __init__(self):
        self.file_name = "cards.json"
        with open(self.file_name, "r") as f:
            data = json.load(f)
            self.cards = {c.get('name'): c for c in data}
    
    def get_desc(self, cards):
        desc = [f"{c}\nKeywords: {self.cards[c].get('keywords')}" for c in cards]
        return "-----".join(desc)
    
    @property
    def card_names(self):
        return list(self.cards.keys())




class TarotApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(ReadingScreen(name='reading')),
        sm.add_widget(KeyScreen(name='key'))
        return sm
    

if __name__ == '__main__':
    TarotApp().run()
