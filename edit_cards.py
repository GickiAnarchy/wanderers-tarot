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
    deck.chooseStack()

if __name__ == "__main__":
    #one_by_one()
    searchCards()