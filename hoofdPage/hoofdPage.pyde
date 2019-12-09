import antwoorden, kaarten, menu, kaartjes, personInfo, modus, Eindpagina#, dice

def setup():
    global page, ant, mode, winnendescore#, die_1, die_2
    
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
    global page, ant, mode, winnendescore#, die_1, die_2
    
    
    #print(dice.die_1)
    
    
    
    background(255)
    if page == "modus":
        modus.draw()
    
    if page == "menu":
        menu.draw(mode)
#hier wordt in de functie gecheckt of een van de players al een winnende score heeft
        j = 0
        while j < len(personInfo.playerList) and mode == "volledige versie":
            if personInfo.playerList[j].wokeScore <= 0 or personInfo.playerList[j].litScore >= winnendescore:
                page = "Eindpagina"
            j += 1
        if mode == "verkorte versie":
            round = calcRound(len(personInfo.playerList), personInfo.turnCount) 
            if round > 19:
                 page = "Eindpagina"
            if personInfo.playerList[j].wokeScore <= 0 or personInfo.playerList[j].litScore >= winnendescore:
                 page = "Eindpagina"
      

        
    if page == "kaarten":
        kaarten.draw()
    
    if page == "antwoorden":
        antwoorden.draw(ant)
        
    if page == "eindpagina":
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
    global page, ant, mode
    
    if page == "modus":
        page, mode = modus.mousePressed()
    
    if  page == "menu":
        page = menu.mousePressed()
        
    if page == "kaarten":
        page,ant = kaarten.mousePressed()
        
    if page == "antwoorden":
        ant, page = antwoorden.mousePressed(ant)
