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
