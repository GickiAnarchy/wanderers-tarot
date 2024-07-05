from tarot import TarotCard, TarotDeck, Spread


def reading():
    #3 card reading.
    reading = Spread()
    reading.draw_cards(3)
    reading.read_cards()


if __name__ == "__main__":
    reading()