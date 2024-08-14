from src.tarot import Reading, SearchCard, ReadCards
from src.serialize import encode_img, decode_img
from src.page_creator import savePage
from src.geminiRequest import pastPresentFuture, celticCross, treeOfLife, simpleReply



def main_menu():
    while True:
        print("What would you like to do?")
        print("Do a Tarot reading: 'R'")
        print("Search for a tarot card: 'S'")
        print("Enter cards to get meaning; 'E'")
        sele = input("Choice: ")
        if sele.lower() not in ["s","r","e","x"]:
            continue
        if sele.lower() == "x":
            break
        if sele.lower() == "r":
            tarot_reading()
            continue
        if sele.lower() == "s":
            search_card()
            continue
        if sele.lower() == "e":
            rc = read_cards()
    print("Thank you. Good luck.")
    return

#
#
#
def tarot_reading():
    reading = Reading()
    sel = reading.go()
    ai_reading = ""
    if sel == 1:
        ai_reading = pastPresentFuture(reading)
    if sel == 2:
        ai_reading = celticCross(reading)
    if sel == 3:
        ai_reading = treeOfLife(reading)
    if sel == 4:
        ai_reading = simpleReply(reading)
    print(ai_reading)

#
#
#
def search_card():
    se  = SearchCard()
    se.search()

#
#
#
def read_cards():
    re = ReadCards()
    reading = Reading()
    sel = reading.go(True)
    ai_reading = ""
    if sel == 1:
        re.start(3)
        reading.cards = re.cards
        ai_reading = pastPresentFuture(reading)
    if sel == 2:
        re.start(10)
        reading.cards = re.cards
        ai_reading = celticCross(reading)
    if sel == 3:
        re.start(10)
        reading.cards = re.cards
        ai_reading = treeOfLife(reading)
    print(ai_reading)

#
#
#
if __name__ == "__main__":
    #decode_img()
    main_menu()
