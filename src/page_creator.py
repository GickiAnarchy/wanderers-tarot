from airium import Airium
#from tarot import *

wtpage = Airium()

def savePage(reading):
    wtpage('<!DOCTYPE html>')
    with wtpage.html(lang="pl"):
        with wtpage.head():
            wtpage.meta(script="type=\"module\" src=\"https://pyscript.net/releases/2023.12.1/core.js")
            wtpage.meta(charset="utf-8")
            wtpage.title(_t=f"Wanderer's Tarot {reading['date_and_time']}")
    
        with wtpage.body():
            with wtpage.div():
                    wtpage.img(src="/media/wt_splash.jpg", alt='alt text')
                    with wtpage.div():
                        with wtpage.h1(id="id23409231", klass='main_header'):
                            wtpage("Wanderer's Tarot Reading")
            with wtpage.div():
                with wtpage.h2():
                    wtpage("Cards Drawn")
                    
                wtpage( reading["cards_drawn"])
            with wtpage.div():
                with wtpage.h2():
                    wtpage("Reading")
                    wtpage(reading["response"])
                

            
    
    html = str(wtpage)  # casting to string extracts the value
    # or directly to UTF-8 encoded bytes:
    html_bytes = bytes(wtpage)  # casting to bytes is a shortcut to str(wtpage).encode('utf-8')
    
    print(html)
    with open(f"src/readings/{reading['date_and_time']}.html","wb") as f:
        f.write(html_bytes)


if __name__ == "__main__":
    testPage()