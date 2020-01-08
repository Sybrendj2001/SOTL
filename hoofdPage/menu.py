import personInfo, random, kaarten

def setup():
    global imgKans, imgStrijd, imgStop, imgCon, imgBack, imgBord, imgBook, dobbel1, dobbel2, drawInventory
    
    dobbel1 = 1
    dobbel2 = 1
    
    imgKans = loadImage("achterkant_kans2.jpeg")
    imgStrijd = loadImage("achterkant_strijd2.jpeg")
    imgBook = loadImage("book1.png")
    imgBord = loadImage("bordPic.png")
    imgStop = loadImage("stop.png")
    imgCon = loadImage("continue.png")
    drawInventory = False

def draw(mode):
    global imgKans, imgStrijd, imgStop, imgCon, imgBack, imgBord,imgBook, dobbel1, dobbel2, drawInventory
    
    j = 1
    y = 1
    
    while j < 7:
        if j == dobbel1:
            dice1 = loadImage("dice" + str(j) + ".png")
        j += 1
    
    while y < 7:
        if y == dobbel2:
            dice2 = loadImage("dice" + str(y) + ".png")
        y += 1
        
    image(dice1,40,40,90,90)
    image(dice2,150,40,90,90)
    
    i = 0    
    textAlign(CENTER,CENTER)
    
    #InventorySlot
    textSize(37)
    fill(19, 249, 19)
    rect(((width/2) - 50), height - 100, 100, 50) # Will later be a picture
    text("Inventory", width / 2, height - 150)
    displayInventory(drawInventory)
    
    fill(255)
    rect(39,149,202,134)
    rect(39,301,202,134)
    
    image(imgStrijd,40,150,200,132)
    image(imgKans,40,302,200,132)
    image(imgCon,90,454,100,100)
    image(imgBook,40,height-150,100,120)
    image(imgBord,width/2-445,height/2-250,890,500)
    
    textSize(37)
    textAlign(CENTER,CENTER)
    text("SURVIVAL OR THE LITTEST\nMENU",(width/2)-250,0,500,150)
    
    evenN = 150
    evenR = 170
    evenP = 190
    evenK = 210
    
    oddN = 150
    oddR = 170
    oddP = 190
    oddK = 210
    
    textAlign(LEFT,CENTER)
    textSize(18)
    while  i < len(personInfo.playerList):
        if i%2 == 0:
            n = personInfo.playerList[i].name
        
            if personInfo.playerList[i].role == "woke":
                p = personInfo.playerList[i].wokeScore
            else:
                p = personInfo.playerList[i].litScore
            
            text(n,width/3-95,evenN,190,40)
            text(personInfo.playerList[i].role,width/3-95,evenR,190,40)
            text("Punten: " + str(p),width/3-95,evenP,190,40)
            
            evenN = evenN + 180
            evenR = evenR + 180
            evenP = evenP + 180
            evenK = evenK + 180
            
        else:
            n = personInfo.playerList[i].name
        
            if personInfo.playerList[i].role == "woke":
                p = personInfo.playerList[i].wokeScore
            else:
                p = personInfo.playerList[i].litScore
            
            text(n,((width/3)*2)+95,oddN,190,40)
            text(personInfo.playerList[i].role,((width/3)*2)+95,oddR,190,40)
            text("Punten: " + str(p),((width/3)*2)+95,oddP,190,40)
            
            oddN = oddN + 180
            oddR = oddR + 180
            oddP = oddP + 180
            oddK = oddK + 180

        i += 1
    
    stroke(255,128,0)
    noFill()
    for i in range(0, len(personInfo.playerList)):
        if personInfo.playerList[i] == personInfo.currentPlayer:
            if i % 2 == 0:
                rect(width/3-100,140 + (i//2 * 180),150,100)
            else:
                rect(((width/3)*2)+90,140 + (i//2 * 180),150,100)
    noFill()
    
    textAlign(RIGHT,CENTER)
    text(str(mode),width-210,0,200,50)
    image(imgStop,width-120,70,100,100)
    text("Eindig het spel",width-210,140,200,80)
    
def displayInventory(a):
    if a == True:
        cp = personInfo.currentPlayer
        k = 0
        for i in cp.strijdInv:
            dataPlace = 400 + k * 150
            fill(19,19,230)
            rect(1400, dataPlace, 100, 50)
            fill(255)
            textSize(35)
            textAlign(LEFT,CENTER)
            text(i, 1400, dataPlace + 20)
            k += 1
            
def assignStrijdToPlayer(a):
    cp = personInfo.currentPlayer
    gevolg = ""
    if a == 0:
        gevolg = cp.strijdInv[a]
    elif a == 1:
        gevolg = cp.strijdInv[a]
    elif a == 2:
        gevolg = cp.strijdInv[a]
    whatToGet = 0
    if "min" in gevolg:
        whatToGet -= int(gevolg[-1])
    elif "plus" in gevolg:
        whatToGet += int(gevolg[-1])
    else:
        whatToGet = 0
    assignee = personInfo.input("Wie ga je de strijdkaart geven")
    for name in personInfo.playerList:
        if name.name == assignee:
            if name.role == "woke":
                name.wokeScore += whatToGet
            elif name.role == "lit":
                name.litScore += whatToGet
    cp.strijdInv.remove(gevolg)
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed():
    global drawInventory
    page = "menu"
    
    if isMouseWithinSpace(39,149,202,134):
        page = "strijd"
        
    if isMouseWithinSpace(40,height-150,100,120):
        page = "spelregels"
        
    if isMouseWithinSpace(width-120,70,100,100):
        page = "eindpagina"
        
    if isMouseWithinSpace(39,301,202,134):
        kaarten.setup()
        page = "kaarten"
        
    if isMouseWithinSpace(40,40,200,90):
        dice()
    
    if isMouseWithinSpace(90,454,100,100):
        personInfo.turnIncrement()

    if isMouseWithinSpace(((width/2) - 50), height - 100, 100, 50):
        drawInventory = not drawInventory
        
    if drawInventory == True:
        if isMouseWithinSpace(1400,400,100,50):
            assignStrijdToPlayer(0)
        elif isMouseWithinSpace(1400,550,100,50):
            assignStrijdToPlayer(1)
        elif isMouseWithinSpace(1400,700,100,50):
            assignStrijdToPlayer(2)
        elif isMouseWithinSpace(1400,950,100,50):
            assignStrijdToPlayer(3)
    return page

def dice():
    global dobbel1, dobbel2
    
    dobbel1 = random.randint(1,6)
    dobbel2 = random.randint(1,6)
