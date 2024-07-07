from tarot import Reading, SearchCard


def main_menu():
    while True:
        print("What would you like to do?")
        print("Do a Tarot reading: 'R'")
        print("Search for a tarot card: 'S'")
        sele = input("Choice: ")
        if sele.lower() not in ["s","r","x"]:
            continue
        if sele.lower() == "x":
            break
        if sele.lower() == "r":
            tarot_reading()
            continue
        if sele.lower() == "s":
            search_card()
            continue
    print("Thank you. Good luck.")
    return

#
#
#
def tarot_reading():
    reading = Reading()
    reading.draw_cards(reading.ask_amount())
    print(reading.get_reading())

#
#
#
def search_card():
    se  = SearchCard()
    print(se.yes_or_no())


if __name__ == "__main__":
    main_menu()