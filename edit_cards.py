from tarot import TarotCard, TarotDeck
from serialize import *

deck = TarotDeck(deck=load_tarot_deck())


def one_by_one():
    for card in deck:
        card.display()
        inp = input("\nEdit this card? \n\tEnter \"y\" to edit meaning.\n\tEnter \"x\" to exit and save.")
        if inp.lower() == "y":
            card.change_meaning()
        elif inp.lower() == "x":
            save_tarot_deck(deck)
            break
        else:
            continue

def testPrint():
    for c in deck:
        c.showMeanings()

def searchCards():
    while True:
        print("Lets search for a card.")
        print(f"\tMA: Sesrch the Major Arcana.")
        print(f"S: Search Stones")
        print(f"F: Search Feathers")
        print(f"M: Search Moons")
        print(f"K: Search Knives")
        s1 = input("What is your choice?")
        match s1.lower():
            case "ma":
                pass
            case "s":
                pass
            case "f":
                pass
            case "m":
                pass
            case "k":
s                pass


if __name__ == "__main__":
    print("EDIT IS BROKEN")
    #one_by_one()
    testPrint()