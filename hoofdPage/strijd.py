import kaartjes, personInfo, random
from datetime import datetime

def setup():
    global imgBack, currentTime, currentMs, timerOO, currentCard, cardDrawn, cardText, pressed, startTime, timerDone, personToGetCard

    cardText = ""
    personToGetCard = ""
    
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
    #Images for the page
    imgStrijd = loadImage("achterkant_strijd2.jpeg")
    imgCard = loadImage("strijd.jpeg")
    image(imgStrijd,40,302,200,132)
    image(imgCard,width/2-400,height/2-264,800,528)

    #Timer Button
    fill(255)
    rect(1300,200,200,50)
    textSize(25)
    text("Start Timer", 1375, 150)
    
    #draw cardtext
    fill(0)
    text(str(selectCard()), width/2-225,250,450,400)
    
    #Assign a card
    fill(255)
    rect(1300,350,200,50)
    text("Assign", 1375, 300)

    if cardDrawn == False:
        cardText = selectCard()
        cardDrawn = True
    
    if timerOO == True:
        trackTime()
    
    if timerDone == True:
        fill(245, 19, 19)
        text("Time's up!", 1400, 600)

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
            text("Keep going!", 1400, 600)

def selectCard():
    global currentCard
    textForQuestion = kaartjes.strijdKaarten[currentCard][0]
    return textForQuestion

def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed():
    global pressed, timerOO, personToGetCard
    page = "strijd"
    if isMouseWithinSpace(1300,200,200,50) and pressed < 1 and timerOO == False:
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
    if isMouseWithinSpace(1300,350,200,50) and pressed < 1:
        endStrijd()
        page = "menu"
        pressed = 1
    pressed = 0
    return page

def endStrijd():
    completed = False
    whatToGet = cardGevolg()
    personToGetCard = personInfo.input("Vul de naam in van de speler die de kaart krijgt:")
    for i in personInfo.playerList:
        if i.name == personToGetCard:
            completed = True
            kaartjes.strijdKaarten.remove(kaartjes.strijdKaarten[0])
            personInfo.turnIncrement()
            i.strijdInv.append(whatToGet)
            setup()
    if completed == False:
        endStrijd()

def cardGevolg():
    x = random.randint(0,6)
    y = random.randint(1,2)
    ans = ""

    if x == 0:
        return x
    
    if y == 1:
        return "min" + str(x)
    else:
        return "plus" + str(x)
    return ans

def givePlayerCard():
    global currentCard
    name = ""
    personInfo[name].strijdInv[strijdInv.len() + 1] = cardGevolg()
    currentCard += 1
    page = "Menu"

#add to playerinfo:
#Inventory
