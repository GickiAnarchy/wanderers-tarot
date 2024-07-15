from airium import Airium
#from tarot import *

wtpage = Airium()

def testPage():
    wtpage('<!DOCTYPE html>')
    with wtpage.html(lang="pl"):
        with wtpage.head():
            wtpage.meta(charset="utf-8")
            wtpage.title(_t="Wanderer's Tarot")
    
        with wtpage.body():
            with wtpage.h1(id="id23409231", klass='main_header'):
                wtpage("Wanderer's Tarot Reading")
            with wtpage.div():
                wtpage.img(src="html/media/wt_splash.jpg", alt='alt text')
                wtpage('the text')
    
    html = str(wtpage)  # casting to string extracts the value
    # or directly to UTF-8 encoded bytes:
    html_bytes = bytes(wtpage)  # casting to bytes is a shortcut to str(wtpage).encode('utf-8')
    
    print(html)
    with open("../test.html","wb") as f:
        f.write(html_bytes)


if __name__ == "__main__":
    testPage()