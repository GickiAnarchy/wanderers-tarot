from cardsjson import number_strings, major_cards


class TarotCard:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
    
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    def display(self):
        for k,v in self.__dict__.items():
            print(f"{k}:\n\t{v}")

    def getDict(self,exclude_attributes=None):
        if exclude_attributes is None:
            exclude_attributes = []
        return {key: value for key, value in self.__dict__.items() if key not in exclude_attributes}
    
    def showMeanings(self):
        print("\n")
        print(self.name)
        print(f"\t{self.keywords}")
        for k,v in self.__dict__.items():
            if k.lower() == "meanings":
                for t,m in self.meanings.items():
                    print(f"{t}::")
                    print(f"\t{m}")



class TarotDeck:
    def __init__(self, deck):
        self.deck = deck
    
    def __iter__(self):
        return iter(self.deck)
    
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
        majors = []
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
        stack = []
        card = None
        while True:
            print("Lets search for a card.")
            print(f"\tMA: Sesrch the Major Arcana.")
            print(f"S: Search Stones")
            print(f"F: Search Feathers")
            print(f"M: Search Moons")
            print(f"K: Search Knives")
            suit = input("What is your choice?")
            if suit.lower() not in ["s","f","m","k","ma"]:
                print("suit not a valid choice")
                break
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
            card.showMeanings()
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