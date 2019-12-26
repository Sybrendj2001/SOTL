import antwoorden, kaarten, menu, kaartjes, personInfo, modus, Eindpagina, spelregels, strijd
from random import shuffle

def setup():
    global page, ant, mode, backImg, spelregel, kaart
    
    size(1600,900)
    
    kaart = 0
    ant = "niets"
    page = "modus"
    mode = " "
    backImg = loadImage("304659.jpg")
    spelregel = 0
    
    personInfo.setup()
    menu.setup()
    spelregels.setup()
    kaarten.setup()
    kaartjes.setup()
    strijd.setup()
    Eindpagina.setup()
    
    
def draw():
    global page, ant, mode, backImg, spelregel, kaart
    
    background(255)
    image(backImg,0,0,1712,963)
    
    if kaart % len(kaartjes.kansEnKennis) == 0 and kaart != 0:
        shuffle(kaartjes.kansEnKennis)
        
    if page == "modus":
        modus.draw()
    
    if page == "menu":
        menu.draw(mode)
        spelregel = 0
        
        j = 0
        while j < len(personInfo.playerList) and mode == "volledige versie":
            if personInfo.playerList[j].wokeScore <= 0 or personInfo.playerList[j].litScore >= 100:
                page = "Eindpagina"
            j += 1
    
    if page == "spelregels":
        spelregels.draw(spelregel)
    
    if page == "kaarten":
        kaarten.draw()
        spelregel = 1
    
    if page == "antwoorden":
        antwoorden.draw(ant)
        spelregel = 2
        
    if page == "eindpagina":
        Eindpagina.draw()
        
    if page == "strijd":
        strijd.draw()
        spelregel = 3

def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    
    
def mousePressed():
    global page, ant, mode, spelregel, kaart
    
    if page == "modus":
        page, mode = modus.mousePressed()
    
    if page == "menu":
        page = menu.mousePressed()
        
    if page == "kaarten":
        page,ant = kaarten.mousePressed()
        kaart +=1
        
    if page == "antwoorden":
        ant, page = antwoorden.mousePressed(ant)
    
    if page == "strijd":
        page = strijd.mousePressed()
        
    if page == "spelregels":
        page = spelregels.mousePressed(spelregel)
