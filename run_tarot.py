from src.tarot import Reading, SearchCard
from src.serialize import encode_img, decode_img
from src.page_creator import savePage
from src.geminiRequest import pastPresentFuture, celticCross, treeOfLife



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
    sel = reading.go()
    ai_reading = ""
    if sel == 1:
        ai_reading = pastPresentFuture(reading)
    if sel == 2:
        ai_reading = celticCross(reading)
    if sel == 3:
        ai_reading = treeOfLife(reading)
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
if __name__ == "__main__":
    #decode_img()
    main_menu()
