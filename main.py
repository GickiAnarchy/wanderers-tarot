from app import TarotApp
import kivy_pydroid


if __name__ == "__main__":
    ta = TarotApp()
    ta.run()




"""


class InputScreen(Screen):
    def submit(self, instance):
        kscreen = self.manager.get_screen('key')
        if not kscreen.check_key():
            self.manager.current = 'key'
            return
        cc = 10
        self.question = self.ids.user_q.text
        question = self.question
        if question.strip():
            if "basica(" in question:
                question = question.replace("DEBUG","")
                cc = 2
            reading_screen = self.manager.get_screen('reading')
            reading_screen.start_reading(question, cc)
            self.manager.current = 'reading'

    def read_celtic(self,instance):
        reading_screen = self.manager.get_screen('reading')
        reading_screen.start_reading(self.question, 10)
        self.manager.current = 'reading'
    
    def read_basic(self,instance):
        reading_screen = self.manager.get_screen('reading')
        reading_screen.start_reading(self.question, 2)
        self.manager.current = 'reading'
    
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




"""