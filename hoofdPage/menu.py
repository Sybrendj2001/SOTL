import personInfo, random

def setup():
    global imgKans, imgStrijd, imgStop, imgCon, imgBack, imgBord, imgBook, dobbel1, dobbel2
    
    dobbel1 = 1
    dobbel2 = 1
    
    imgKans = loadImage("achterkant_kans2.jpeg")
    imgStrijd = loadImage("achterkant_strijd2.jpeg")
    imgBook = loadImage("book1.png")
    imgBord = loadImage("bordPic.png")
    imgStop = loadImage("stop.png")
    imgCon = loadImage("continue.png")

def draw(mode):
    global imgKans, imgStrijd, imgStop, imgCon, imgBack, imgBord,imgBook, dobbel1, dobbel2
    
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
    
    fill(255)
    
    rect(39,149,202,134)
    rect(39,301,202,134)
    
    image(imgStrijd,40,150,200,132)
    image(imgKans,40,302,200,132)
    image(imgCon,90,454,100,100)
    image(imgBook,40,height-150,100,120)
    image(imgBord,width/2-445,height/2-250,890,500)
    
    textSize(37)
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
            text("Strijdkaarten: ",width/3-95,evenK,190,40)
            
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
            text("Strijdkaarten: ",((width/3)*2)+95,oddK,190,40)
            
            oddN = oddN + 180
            oddR = oddR + 180
            oddP = oddP + 180
            oddK = oddK + 180

        i += 1
        
    textAlign(RIGHT,CENTER)
    text(str(mode),width-210,0,200,50)
    image(imgStop,width-120,70,100,100)
    text("Eindig het spel",width-210,140,200,80)
        

def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False


def mousePressed():
    
    page = "menu"
    
    if isMouseWithinSpace(39,149,202,134):
        page = "strijd"
        
    if isMouseWithinSpace(40,height-150,100,120):
        page = "spelregels"
        
    if isMouseWithinSpace(width-120,70,100,100):
        page = "eindpagina"
        
    if isMouseWithinSpace(39,301,202,134):
        page = "kaarten"
        
    if isMouseWithinSpace(40,40,200,90):
        dice()
    
    if isMouseWithinSpace(90,454,100,100):
        personInfo.turnIncrement()
            
    return page

def dice():
    global dobbel1, dobbel2
    
    dobbel1 = random.randint(1,6)
    dobbel2 = random.randint(1,6)
    
    
