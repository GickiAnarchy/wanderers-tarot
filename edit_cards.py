from tarot import TarotCard, TarotDeck, Spread


def reading():
    #3 card reading.
    reading = Spread()
    reading.draw_cards(3)
    reading.read_cards()
    print(reading.reading.get_reading())


if __name__ == "__main__":
    reading()