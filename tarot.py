import random
import datetime
from cardsjson import number_strings, major_cards
from serialize import *


class TarotCard:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
            self.isReversed = None
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def drawn(self):
        self.isReversed = random.choice(["u","r"])

    def lay_down(self):
        delimiter = " : "
        mean = ""
        if self.isReversed:
            mean = f"(Reversed):\n\t"
            mean = mean + delimiter.join(self.meanings["shadow"])
        else:
            mean = f"(Upright):\n\t"
            mean = mean + delimiter.join(self.meanings["light"])
        ret = f"{str(self.number)}::{self.name}"
        r2 = f"Keywords:\n{delimiter.join(self.keywords)}"
        r3 = f"Meaning{mean}"
        tot = f"{ret}\n{r2}\n{r3}"
        print(self.name)
        return tot

    def display(self):
        for k,v in self.__dict__.items():
            print(f"{k}:\n\t{v}")

    def getDict(self,exclude_attributes=None):
        exclude_attributes = []
        return {key: value for key, value in self.__dict__.items() if key not in exclude_attributes}
    
    """
    def showMeanings(self):
        print("\n")
        print(self.name)
        print(f"\t{self.keywords}")
        ret = ""
        for k,v in self.__dict__.items():
            if k.lower() == "meanings":
                if self.isReversed == "r":
                    pos = "Reversed"
                    ret = f"{pos}\n{self.meanings['shadow']}"
                if self.isReversed == "u":
                    pos = "Upright"
                    ret = f"{pos}\n{self.meanings['light']}"
                if self.isReversed == None:
                    print("Card hasnt been pulled")
        return ret
    """
                
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
        self.showChosen()
        return
    
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
class Spread:
    def __init__(self):
        self.deck = TarotDeck()
        self.pulled_cards = []
        self.reading = None

    def draw_cards(self, amount, reshuffle = True):
        if reshuffle:
            for c in self.pulled_cards:
                self.deck.append(c)
            self.deck.shuffle()
        for i in range(amount):
            self.pulled_cards.append(self.deck.pullCard())
            
    def read_cards(self):
        self.reading = Reading(self.pulled_cards)
        if not self.pulled_cards:
            print("No cards are pulled")
        for card in self.pulled_cards:
            card.lay_down()
            print(f"\n")
            cont = input("...")
            if cont in [""," "]:
                continue
            if cont.lower() == "x":
                break

#
#
class Reading:
    def __init__(self, cards, saving = None):
        self.cards = cards
        self.saving = saving
    
    def get_reading(self):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%m/%d/%Y %H:%M")
        self.saving = []
        self.saving.append(f"{formatted_date}")
        for card in self.cards:
            self.saving.append(card.lay_down())
        self.save_reading()
        return self.saving
    
    def save_reading(self):
        delimiter = "\n"
        read_str = delimiter.join(self.saving)
        save_readings(read_str)
        
        