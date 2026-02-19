### MAIN.PY
################

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


class InputScreen(Screen):
    def submit(self, instance):
        cc = 10
        question = self.ids.user_q.text
        if question.strip():
            if "DEBUG" in question:
                question = question.replace("DEBUG","")
                cc = 2
            reading_screen = self.manager.get_screen('reading')
            reading_screen.start_reading(question, cc)
            self.manager.current = 'reading'

class ReadingScreen(Screen):
    def start_reading(self, question, cc = 10):
        ccount = cc
        self.ids.status.text = "The cosmic energies are aligning..."
        threading.Thread(target=self.generate_reading, args=(question,ccount)).start()

    def generate_reading(self, question, card_count = 10):
        card_count = card_count
        try:
            cards = Cards()
            drawn_cards = random.sample(cards.card_names, card_count)
            card_str = cards.get_desc(drawn_cards)
            drawn = ", ".join(drawn_cards)
            instruct = "Determine an insightful response for the seekers inquiry with the cards drawn."
            
            if card_count == 10 and os.path.exists("celtic_cross.txt"):
                with open("celtic_cross.txt","r") as f:
                    instruct = f.read()
            
            if card_count == 2:
                instruct = "Answer with a simple one word response i.e. 'Yes','No','Maybe'."
            
            prompt = (
                f"User Question: '{question}'. Cards: {card_str}. " \
                f"{instruct}"
            )
            
            response = generate(prompt)
             
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



### GEN.PY
#############

# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate(inquiry=None):
    if inquiry is None:
        inquiry = "Am I gonna be ok?"
        
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=inquiry),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1.95,
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        system_instruction=[
            types.Part.from_text(text="You are a tarot card reader. You are insightful yet completely honest. You answer the questions and inquiries of seekers while keeping things brief and to the point"),
        ],
    )

    full_response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
        if chunk.text:
            full_response += chunk.text

    return full_response
        

if __name__ == "__main__":
    generate()


