import antwoorden, kaarten, menu, kaartjes, personInfo, modus, Eindpagina, spelregels, strijd

def setup():
    global page, ant, mode, backImg
    
    size(1600,900)
    
    ant = "niets"
    page = "modus"
    mode = " "
    backImg = loadImage("304659.jpg")
    
    personInfo.setup()
    kaarten.setup()
    kaartjes.setup()
    strijd.setup()
    
def draw():
    global page, ant, mode, backImg
    
    background(255)
    image(backImg,0,0,1712,963)
    if page == "modus":
        modus.draw()
    
    if page == "menu":
        menu.draw(mode)
        
        j = 0
        while j < len(personInfo.playerList) and mode == "volledige versie":
            if personInfo.playerList[j].wokeScore <= 0 or personInfo.playerList[j].litScore >= 100:
                page = "Eindpagina"
            j += 1
    if page == "spelregels":
        spelregels.draw(mode)
    
    if page == "kaarten":
        kaarten.draw()
    
    if page == "antwoorden":
        antwoorden.draw(ant)
        
    if page == "eindpagina":
        Eindpagina.draw()
        
    if page == "strijd":
        strijd.draw()

def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    
    
def mousePressed():
    global page, ant, mode
    
    if page == "modus":
        page, mode = modus.mousePressed()
    
    if page == "menu":
        page = menu.mousePressed()
        
    if page == "kaarten":
        page,ant = kaarten.mousePressed()
        
    if page == "antwoorden":
        ant, page = antwoorden.mousePressed(ant)
    if page == "strijd":
        page = strijd.mousePressed()
