__version__ = "1.0.0"

import os
from dotenv import load_dotenv
import random
import threading
import json
import certifi
import requests  # Replaces google-generativeai
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.image import Image
from gen import generate


load_dotenv()

# --- SSL Configuration for Android ---
# This ensures the app can make secure HTTPS calls to Google's servers
#os.environ['SSL_CERT_FILE'] = certifi.where()

# --- GOOGLE AI CONFIGURATION ---
#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GOOGLE_API_KEY}"

class InputScreen(Screen):
    def submit(self, instance):
        question = self.ids.user_q.text
        if question.strip():
            reading_screen = self.manager.get_screen('reading')
            reading_screen.start_reading(question)
            self.manager.current = 'reading'

class ReadingScreen(Screen):
    def start_reading(self, question):
        self.ids.status.text = "The cosmic energies are aligning..."
        threading.Thread(target=self.generate_reading, args=(question,)).start()

    def generate_reading(self, question):
        try:
            cards = Cards()
            drawn_cards = random.sample(cards.card_names, 10)
            card_str = cards.get_desc(drawn_cards)
            drawn = ", ".join(drawn_cards)
            instruct = ""
            if os.path.exists("celtic_cross.txt"):
                with open("celtic_cross.txt","r") as f:
                    instruct = f.read()
            
            prompt = (
                f"User Question: '{question}'. Cards: {card_str}. " \
                f"{instruct}"
            )
            
            response = generate(prompt,"celtic")
             
            final_text = f"The Cards: {drawn}\n\n{response}"
            Clock.schedule_once(lambda dt, res=final_text: self.update_ui(res, "The Oracle has spoken."))
            
        except Exception as e:
            error_str = str(e)
            Clock.schedule_once(lambda dt, err=error_str: self.update_ui(f"The connection was lost: {err}", "Error"))

    def update_ui(self, text, status):
        self.ids.reading_label.text = text
        self.ids.status.text = status

    def go_back(self, instance):
        self.manager.current = 'input'
        self.ids.reading_label.text = ""

class Cards:
    def __init__(self):
        self.file_name = "cards.json"
        self.load_cards()
        self.get_cards()
    
    def load_cards(self):
        with open(self.file_name, "r") as f:
            self.cards = json.load(f)
    
    def get_cards(self):
        self.cards = {c.get('name'): c for c in self.cards}
    
    def get_desc(self, cards):
        desc = []
        for c in cards:
            s = f"{c}\nKeywords: {self.cards[c].get('keywords')}"
            desc.append(s)
        return "-----".join(desc)
    
    @property
    def card_names(self):
        return list(self.cards.keys())

class TarotApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(ReadingScreen(name='reading'))
        return sm

if __name__ == '__main__':
    TarotApp().run()
