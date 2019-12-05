<<<<<<< Updated upstream
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
=======
import antwoorden, kaarten, menu, kaartjes, personInfo, modus, Eindpagina, dice

def setup():
    global page, ant, mode, winnendescore, die_1, die_2
    
    size(1600,900)
    
    ant = "niets"
    page = "modus"
    mode = " "
    winnendescore = 100
    
    personInfo.setup()
    kaarten.setup()
    kaartjes.setup()
    print(winnendescore)
    

    
def draw():
    global page, ant, mode, winnendescore, die_1, die_2
    ###########print(dice.die_1)
    background(255)
    if page == "modus":
        modus.draw()
    
    if page == "menu":
        menu.draw(mode)
#hier wordt in de functie gecheckt of een van de players al een winnende score heeft
        j = 0
        while j < len(personInfo.playerList) and mode == "volledige versie":
            if personInfo.playerList[j].wokeScore >= winnendescore or personInfo.playerList[j].litScore >= winnendescore:
                page = "Eindpagina"
            j += 1
        if mode == "verkorte versie":
            round = calcRound(len(personInfo.playerList), personInfo.turnCount) 
            if round > 19:
                 page = "Eindpagina"
            if personInfo.playerList[j].wokeScore <= 0 or personInfo.playerList[j].litScore >= winnendescore:
                 page = "Eindpagina"
      

        
    if page == "kaarten":
>>>>>>> Stashed changes
        kaarten.draw()
        
    elif page == "antwoorden":
        antwoorden.draw(ant)
        
    elif page == "modus":
        modus.draw()
        
    elif page == "Eindpagina":
        Eindpagina.draw()

def calcRound(playeraantal, turncount):
    roundnumber= turncount//playeraantal
    return roundnumber

              
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
    

    
