from cardsjson import number_strings, major_cards


class TarotCard:
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
    
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
    
    def getMajors(self):
        majors = []
        for c in deck:
            if c.arcana == "Major Arcana":
                majors.append(c)
        return majors

    def getMoons(self)        moons = []
            for c in deck:
                if c.suit == "Moons":
                    moons.append(c)
            return moons

    def getStones(self):
        majors = []
            for c in deck:
                if c.suit == "Stones":
                    stones.append(c)
            return stones

    def getFeathers(self):
        feathers = []
            for c in deck:
                if c.suit == "Feathers":
                    feathers.append(c)
            return feathers

    def getKnives(self):
        knives = []
            for c in deck:
                if c.suit == "Knives":
                    knives.append(c)
            return knives