import os
import random
import threading
import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from gen import generate



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

