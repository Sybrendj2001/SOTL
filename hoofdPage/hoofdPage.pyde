import kaarten, menu, antwoorden, personInfo, modus

def setup():
    global page, score, vraag, ant
    score = 0
    page = "modus"
    ant = "niets"
    vraag = 0
    personInfo.setup()
    kaarten.setup(vraag)
    size(800,800)

    #hallo
            
def draw():
    global page, ant
    
    if page == "menu":
        menu.draw()
        imgKans = loadImage("achterkant_kans2.jpeg")
        imgStrijd = loadImage("achterkant_strijd2.jpeg")
        image(imgKans,500,200,200,132)
        image(imgStrijd,500,450,200,132)
#Hier wordt continue gecheckt of een speler al 100 punten heeft of meer
        i = 0 
        while i < len(personInfo.playerList):
            if personInfo.playerList[i].wokeScore >= 100 or personInfo.playerList[i].litScore >= 100:
                    page = "Eindpagina"
            i += 1
        
#Hier worden de pagina's veranderd, wanneer de string van page gelijk is aan de naam van de nieuwe pagina.         
    elif page == "kans/kenniskaarten":
        kaarten.draw()
        
    elif page == "antwoorden":
        antwoorden.draw(ant)
        
    elif page == "modus":
        modus.draw()
        
    elif page == "Eindpagina":
        Eindpagina.draw()


def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

    
    
def mousePressed():
    global score, page, vraag, kenniskaarten, ant
    
    if isMouseWithinSpace(499,199,202,134) and page == "menu":
        page = "kans/kenniskaarten"
        vraag = kaarten.randomKaart()
        
    if page == "kans/kenniskaarten":
        ant = kaarten.mousePressed()
        if ant != "niets":
            page = "antwoorden"
    #TODO: laat alle methodes hier hun input returnen als default
    if page == "antwoorden":
        ant1,page1 = antwoorden.mousePressed(ant,vraag)
        
        if ant1 != None:
            ant = ant1
        
        if page1 != None:
            page = page1
            
    if page == "modus":
        pageTemp = modus.mousePressed()
        if pageTemp != None:
            page = pageTemp
    

    
