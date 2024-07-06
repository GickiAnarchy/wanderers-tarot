from tarot import Reading


def reading():
    reading = Reading()
    reading.draw_cards(reading.ask_amount())
    print(reading.get_reading())


if __name__ == "__main__":
    reading()