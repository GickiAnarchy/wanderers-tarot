import random
import datetime
from .cardsjson import *
from .serialize import *

#
#
class TarotCard:
    count = 0
    
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
        self.isReversed = None
        TarotCard.count += 1
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    @classmethod
    def getCount(cls):
        return cls.count

    def drawn(self):
        self.isReversed = random.choice(["u","r"])

    def lay_down(self):
        #Init
        ret = []
        #Card name and number
        ret.append(f"{str(self.number)}::{self.name}")
        #Keywords
        delim = " : "
        ret.append(f"Keywords:\n{delim.join(self.keywords)}")
        #Meaning
        delimiter = " : "
        mean = ""
        if self.isReversed == "r":
            mean = f"(Reversed):\n\t"
            mean = mean + delimiter.join(self.meanings["shadow"])
        elif self.isReversed == "u":
            mean = f"(Upright):\n\t"
            mean = mean + delimiter.join(self.meanings["light"])
        ret.append(f"Meaning{mean}")
        #Print name to console and return
        print(self.name)
        return ret

    def display(self):
        for k,v in self.__dict__.items():
            print(f"{k}:\n\t{v}")

    def getDict(self,exclude_attributes=None):
        exclude_attributes = []
        return {key: value for key, value in self.__dict__.items() if key not in exclude_attributes}
                
    def showKeywords(self):
        for k in self.keywords:
            print(f"{k:<4}", end = "\t")
    
    def retKeywords(self):
        ret = ""
        for k in self.keywords:
            ret += f"{k:<2}"
        return ret

#
#
class TarotDeck:
    def __init__(self):
        self.deck = []
        self.createDeck()
        self.chosen = []
    
    def __iter__(self):
        return iter(self.deck)

    def createDeck(self):
        for details in load_tarot_deck():
            self.deck.append(TarotCard(**details))

    def shuffle(self):
        for c in self.chosen:
            self.deck.append(c)
        random.shuffle(self.deck)
        print(str(len(self.deck)) + " cards")
        print("Shuffled")
        
    def pullCard(self):
        if not self.deck:
            print("No more cards in the deck")
            return
        else:
            c = self.deck.pop(0)
            c.drawn()
            return c

    def getMajors(self):
        majors = []
        for c in self.deck:
            if c.arcana == "Major Arcana":
                majors.append(c)
        return majors

    def getMoons(self):        
        moons = []
        for c in self.deck:
            if c.suit == "Moons":
                moons.append(c)
        return moons

    def getStones(self):
        stones = []
        for c in self.deck:
            if c.suit == "Stones":
                stones.append(c)
        return stones

    def getFeathers(self):
        feathers = []
        for c in self.deck:
            if c.suit == "Feathers":
                feathers.append(c)
        return feathers

    def getKnives(self):
        knives = []
        for c in self.deck:
            if c.suit == "Knives":
                knives.append(c)
        return knives
    
    def chooseStack(self):
        self.chosen = []
        stack = []
        card = None
        while True:
            print("\n")
            print("Lets search for a card.")
            print(f"\tMA: Sesrch the Major Arcana.")
            print(f"\tS: Search Stones")
            print(f"\tF: Search Feathers")
            print(f"\tM: Search Moons")
            print(f"\tK: Search Knives")
            suit = input("What is your choice?")
            if suit.lower() not in ["s","f","m","k","ma","x"]:
                print("suit not a valid choice")
                continue
            match suit.lower():
                case "ma":
                    stack = self.getMajors()
                case "m":
                    stack = self.getMoons()
                case "s":
                    stack = self.getStones()
                case "f":
                    stack = self.getFeathers()
                case "k":
                    stack = self.getKnives()
                case "x":
                    break
                case _:
                    print("OOOOOPPPPPPPPPSSSSSSS")
            print("Choose a card:")
            self.listSuit(stack)
            print("Enter the number. 'x' to exit. 'b' to go back.")
            card_no = input("Choice:")
            if card_no.lower() == "b":
                continue
            if card_no.lower() == "x":
                break
            try:
                card = stack[int(card_no) - 1]
            except:
                print("Card choice was not valid")
                break
            self.addChosen(card)
            break
        self.showChosen()
        return card
    
    def listSuit(self, stack):
        # Define the number of columns
        num_columns = 3
        # Calculate the number of rows
        num_rows = (len(stack) + num_columns - 1) // num_columns
        for row in range(num_rows):
            for col in range(num_columns):
                index = row + col * num_rows
                if index < len(stack):
                    print(f"{index+1}. {stack[index].name:<10}", end='\t')
            print()

    def addChosen(self, card):
        card.drawn()
        self.chosen.append(card)

    def showChosen(self):
        if len(self.chosen) == 0:
            return
        else:
            i = 0
            for c in self.chosen:
                i += 1
                print(f"{str(i)}-{c.name}::\n")
                print(f"\t{c.showKeywords()}", end = "\n")

#
#
class Reading:
    def __init__(self):
        self.deck = TarotDeck()
        self.cards = []

    def ask_amount(self):
        print("How many cards are you wanting to draw?")
        while True:
            try:
                answer = int(input(f"Enter amount. (no more than {str(TarotCard.getCount())}."))
                return answer
            except ValueError:
                print("That's not an integer!")

    def draw_cards(self, amount, reshuffle = True):
        if reshuffle:
            for c in self.cards:
                self.deck.append(c)
            self.deck.shuffle()
        for i in range(amount):
            self.cards.append(self.deck.pullCard())

    def get_reading(self):
        if not self.cards:
            print("No cards have been pulled")
            return
        reading = []
        time_now = self.getTime()
        for card in self.cards:
            reading.append(card.lay_down())
        reading_dict = {f"{time_now}":reading}
        if self.ask_save():
            self.save_reading(reading_dict)
        return reading
    
    def save_reading(self, reading):
        save_readings(reading)

    def getTime(self):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%m/%d/%Y %H:%M")
        return formatted_date

    def ask_save(self):
        print("Do you want to save this reading?")
        answer = input("'y' for Yes. Any other key to skip.")
        if answer.lower() in ["y","yes","yea","yeah"]:
            return True
        else:
            return False

#
#
class SearchCard:
    def __init__(self):
        self.deck = TarotDeck()
        self.chosen_card = None
        self
        self.suit_options = cardsjson.suit_options
    
    def search(self):
        self.chosen_card = self.deck.chooseStack()
        print(f"Chose {self.chosen_card.name}!")
        input("")
        self.show_card()
        
        """
        print("Lets choose a card.")
        print("Lets first choose the suit the card is in.")
        print("(M)oons, (S)tones, (K)nives, (F)eathers")
        print("The Major Arcana is known as (t)rump suit")
        #Choose the suit
        while True:
            sele = input("Choose Suit: ")
            if sele.lower() in self.gather_options():
                for k,v in self.suit_options.items():
                    if sele.lower() in v:
                        chosen_suit = k
                        print(f"{k} suit chosen."
        #Choose the number.
        num_columns = 3
        num_rows = (len(stack) + num_columns - 1) // num_columns
        for row in range(num_rows):
            for col in range(num_columns):
                index = row + col * num_rows
                if index < len(stack):
                    print(f"{index+1}. {stack[index].name:<15}", end=' | ')
            """

    def show_card(self):
        if self.chosen_card == None:
            print("No chosen card")
            return
        info = json.dumps(self.chosen_card.getDict(), indent = 4)
        print(info)
        

    def gather_options(self):
        ret = []
        for k in self.suit_options.keys():
            for v in self.suit_options[k]:
                print(f"{k}: {v}")
                ret.append(v)
        return ret

    def yes_or_no(self):
        print("(Y)es or (N)o?")
        while True:
            sele = input("Choice: ")
            if sele.lower() not in ["n","y"]:
                continue
            if sele.lower() == "y":
                ret = True
                break
            if sele.lower() == "n":
                ret = False
                break
        return ret

