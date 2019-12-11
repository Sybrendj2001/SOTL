import kaartjes, personInfo, random
from datetime import datetime

def setup():
    global imgBack, currentTime, currentMs, timerOO, currentCard, cardDrawn, cardText, pressed, startTime, timerDone

    cardText = ""
    
    currentTime = 0
    currentMs = 0
    currentCard = 0
    pressed = 0
    startTime = 0
    
    timerOO = False
    cardDrawn = False
    timerDone = False
    
    imgBack = loadImage("back.png")

def draw():
    global cardDrawn, cardText, timerOO, startTime, timerDone
    textAlign(CENTER,CENTER)
    imgStrijd = loadImage("achterkant_strijd2.jpeg")
    image(imgStrijd,40,302,200,132)

    #Timer Button
    fill(255)
    rect(600,200,200,50)
    textSize(25)
    text("Start Timer", 550, 150)

    #Player wins buttons:
    #fill(255)
    #rect(400,200,200,50)
    #textSize(20)
    #text("", 350, 250)

    if cardDrawn == False:
        cardText = selectCard()
        cardDrawn = True
    
    if timerOO == True:
        trackTime()
    
    if timerDone == True:
        text("Time's up!", 600, 600)

def timer():
    timeraw = datetime.now()
    seconds = int(timeraw.strftime("%S"))
    return seconds

def startTimer():
    global startTime, timerOO
    startTime = timer()
    timerOO = True
    
def trackTime():
    global startTime, timerOO, timerDone, rightTime
    if startTime < 30:
        if timer() - 30 >= startTime:
            timerOO = False
            timerDone = True
        else:
            text("Keep going!", 600, 600)
    else:
        if (startTime - timer()) < 30 and timer() < 30:
            timerOO = False
            timerDone = True
        else:
            text("Keep going!", 600, 600)

def selectCard():
    global currentCard
    textForQuestion = kaartjes.strijdKaarten[currentCard]
    currentCard += 1
    return textForQuestion

def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False


def mousePressed():
    global pressed, timerOO
    page = "strijd"
    if isMouseWithinSpace(600,200,200,50) and pressed < 1 and timerOO == False:
        startTimer()
        pressed = 1
    if isMouseWithinSpace(400,200,200,50) and pressed < 1:
        #invoegen met hulp van jullie
        print("")
        page = "menu"
        pressed = 1
    if isMouseWithinSpace(39,300,202,134) and pressed < 1:
        page = "menu"
        pressed = 1
    pressed = 0
    return page

def cardGevolg():
    x = random(1,4)
    ans = ""

    if x == 1:
        ans = "plus 5 litpunten"
    if x == 2:
        ans = "min 5 litpunten"
    if x == 3:
        ans = "plus 5 carbonfootprint"
    if x == 4:
        ans = "min 5 carbonfootprint"
    return ans

def givePlayerCard():
    name = ""
    personInfo[name].strijdInv[strijdInv.len() + 1] = cardGevolg()
    page = "Menu"



#add to playerinfo:
#Inventory
