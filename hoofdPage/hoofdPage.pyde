import antwoorden, kaarten, menu, kaartjes, personInfo, modus, Eindpagina

def setup():
    global page, ant, mode
    
    size(800,800)
    
    ant = "niets"
    page = "modus"
    mode = " "
    
    personInfo.setup()
    kaarten.setup()
    kaartjes.setup()
    
    print(kaartjes.kansEnKennis[0])
    
    
def draw():
    global page, ant, mode
    
    background(255)
    if page == "modus":
        modus.draw()
    
    if page == "menu":
        menu.draw(mode)
        
        j = 0
        while j < len(personInfo.playerList) and mode == "volledige versie":
            if personInfo.playerList[j].wokeScore >= 100 or personInfo.playerList[j].litScore >= 100:
                page = "Eindpagina"
            j += 1
        
    if page == "kaarten":
        kaarten.draw()
    
    if page == "antwoorden":
        antwoorden.draw(ant)
        
    if page == "eindpagina":
        Eindpagina.draw()


def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    
    
def mousePressed():
    global page, ant, mode
    
    if page == "modus":
        page, mode = modus.mousePressed()
    
    if  page == "menu":
        page = menu.mousePressed()
        
    if page == "kaarten":
        page,ant = kaarten.mousePressed()
        
    if page == "antwoorden":
        ant, page = antwoorden.mousePressed(ant)
