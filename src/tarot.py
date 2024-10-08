import random
import datetime
import os
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

    def getAIInfo(self):
        mean = ""
        if self.isReversed == "r":
            mean = ",Reversed"
        elif self.isReversed == "u":
            pass
        ret = f"{self.name}{mean}"
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
    def __init__(self,cards=[],form_date=None):
        self.deck = TarotDeck()
        self.cards = cards
        self.formatted_date = form_date
        self.question = ""

    def getCards(self):
        stuff = []
        if len(self.cards) > 0:
            for c in self.cards:
                stuff.append(f"{c.getAIInfo()}")
            return stuff
        else:
            print("No cards in reading")
 
    def go(self, do_not_draw = False):
        self.askQuestion()
        ret = self.chooseSpread(do_not_draw)
        return ret

    def chooseSpread(self, do_not_draw = False):
        while True:
            print("Choose a reading spread:")
            print("1) Past, Present, Future - 3 cards")
            print("2) Celtic Cross - 10 cards")
            print("3) Tree of Life - 10 cards")
            print("4) Simple Yes or No.")
            sel = input("Enter the number: ")
            try:
                ret = int(sel)
            except:
                print("Must be a number value")
            if ret in [1,2,3,4] and do_not_draw == False:
                match ret:
                    case 1:
                        self.draw_cards(3)
                    case 2:
                        self.draw_cards(10)
                    case 3:
                        self.draw_cards(10)
                    case 4:
                        self.draw_cards(4)
            return ret

    def askQuestion(self):
        print("What is the question you are seeking the answer for?")
        self.question = input("Ask the universe: ")
            
    def ask_amount(self):
        print("How many cards are you wanting to draw?")
        while True:
            try:
                answer = int(input(f"Enter amount. (no more than {str(TarotCard.getCount())})"))
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

    def show_reading(self):
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
    
    def load_reading(self, past_read):
        self.formatted_date = past_read.keys[0]
        self.cards = past_read[f"{self.formatted_date}"]
    
    def view_past(self):
        p_read = load_readings()
        for k,v in p_read.items():
            print(f"{k}: {str(len(v))} cards.")
            stop = input("View Reading?")
            if stop.lower() in ["y","yea","yes",]:
                self.load_reading(p_read[f"{k}"])
            if stop.lower() in ["n","no","nah","nope"]:
                continue
            if stop.lower() in ["x","exit","stop"]:
                break
        
    def getTime(self):
        if self.formatted_date == None:
            now = datetime.datetime.now()
            self.formatted_date = now.strftime("%m/%d/%Y %H:%M")
        return self.formatted_date

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
        self.suit_options = cardsjson.suit_options
    
    def search(self):
        self.chosen_card = self.deck.chooseStack()
        print(f"Chose {self.chosen_card.name}!")
        input("")
        self.show_card()
 
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

#
#
class ReadCards:
    def __init__(self):
        self.cards = []
        self.deck = TarotDeck()

    def start(self, amt:int):
        self.addCard(amt)

    def addCard(self, amt):
        for _ in range(amt):
            crd = self.getCard_one()
            self.cards.append(crd)

    def getCard_one(self):
        card_list = []
        while True:
            print("Search a card to add:")
            print("First, Choose the suit.")
            print("'F' - Feathers       'K' - Knives")
            print("'M' - Moons          'S' - Stones")
            print("'T' - Major Arcana   'X' - Exit")
            suit = input("Enter suit: ")
            if suit.lower() not in ["f","k","m","s","t","x"]:
                print("Not a valid input")
                continue
            else:
                match suit.lower():
                    case "f":
                        card_list = self.deck.getFeathers()
                    case "k":
                        card_list = self.deck.getKnives()
                    case "s":
                        card_list = self.deck.getStones()
                    case "m":
                        card_list = self.deck.getMoons()
                    case "t":
                        card_list = self.deck.getMajors()
            return card_list[self.getCard_two(card_list)]

    def getCard_two(self,selected_suit):
        for c in selected_suit:
            print(f"{c.number})     {c.name}")
        print("Enter the numeral value.")
        sel = input("# ")
        try:
            sel = int(sel)
        except ValueError:
            print("That isn't a correct selection.")
        return sel - 1

    def yes_or_no(self, msg = ""):
        print(msg)
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

