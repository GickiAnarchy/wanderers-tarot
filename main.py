import random
import threading
import json
import google.generativeai as genai
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import env

# --- GOOGLE AI CONFIGURATION ---
GOOGLE_API_KEY = "AIzaSyCYN6l7CXHcDJORSsx4vYSAWsPFdPegHwQ"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

class TarotDeck:
    MAJOR_ARCANA = [
        "The Fool", "The Magician", "The High Priestess", "The Empress",
        "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
        "Strength", "The Hermit", "Wheel of Fortune", "Justice",
        "The Hanged Man", "Death", "Temperance", "The Devil",
        "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"
    ]

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
        # Run in thread to prevent UI freezing
        threading.Thread(target=self.generate_reading, args=(question,)).start()

    def generate_reading(self, question):
        cards = Cards()
        
        drawn_cards = random.sample(cards.card_names, 3)
        card_str = cards.get_desc(drawn_cards)
        drawn = ",".join(drawn_cards)
        
        prompt = (
            f"User Question: '{question}'. Cards: {card_str}. "
            "Provide a short, mystical 3-part tarot reading. Then summarize the reading with a very short response at the end."
        )

        try:
            response = model.generate_content(prompt)
            # Use a variable to hold the text
            final_text = f"The Cards: {drawn}\n\n{response.text}"
            
            # Pass final_text into the lambda as a default arg 'res'
            Clock.schedule_once(lambda dt, res=final_text: self.update_ui(res, "The Oracle has spoken."))
            
        except Exception as e:
            error_str = str(e)
            # Pass error_str into the lambda as a default arg 'err'
            Clock.schedule_once(lambda dt, err=error_str: self.update_ui(f"The connection was lost: {err}", "Error"))

    def update_ui(self, text, status):
        self.ids.reading_label.text = text
        self.ids.status.text = status

    def go_back(self, instance):
        self.manager.current = 'input'
        self.ids.reading_label.text = ""

class TarotApp(App):
    def build(self):
        # This still looks for 'tarot.kv' automatically
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(ReadingScreen(name='reading'))
        return sm

class Cards:
    def __init__(self):
        self.file_name = "cards.json"
        self.load_cards()
        self.get_cards()
    
    def load_cards(self):
        with open(self.file_name, "r") as f:
            self.cards = json.load(f)
    
    def get_cards(self):
        self.cards = {c.get('name'):c for c in self.cards}
    
    def get_desc(self, cards):
        desc = []
        for c in cards:
            s = f"{c}\nKeywords:\n{self.cards[c].get('keywords')}"
            desc.append(s)
        ret = "-----".join(desc)
        print(ret)
        return ret
    
    @property
    def card_names(self):
        return [n for n in self.cards.keys()]


if __name__ == '__main__':
    TarotApp().run()
