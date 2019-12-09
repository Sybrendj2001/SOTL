import kaartjes, personInfo, random

def setup():
    global imgBack, currentTime, currentMs, timerOO, currentCard, cardDrawn, cardText, pressed

    cardText = ""
    
    currentTime, currentMs, currentCard, pressed = 0
    
    TimerOO, cardDrawn = False

    imgBack = loadImage("back.png")

def draw():
    global cardDrawn, cardText, timerOO
    textAlign(CENTER,CENTER)
    imgStrijd = loadImage("achterkant_strijd2.jpeg")
    image(imgStrijd,40,302,200,132)

    #Timer Button
    fill(255)
    rect(600,200,200,50)
    textsize(25)
    text("Start Timer")

    #Player wins buttons:
    fill(255)
    rect(400,200,200,50)
    textsize(20)
    text()

    if cardDrawn == False:
        cardText = selectCard()
        cardDrawn = True

    if timerOO == True:
        timer()
        textSize(20)
        text(str(currentTime))
        if currentTime == 30:
            timerOO = False
            text("Time!")

def timer():
    global currentTime, currentMs
    if currentMs == 60:
        currenttime += 1
        currentMs = 0
    currentMs += 1

def selectCard():
    global currentCard
    textForQuestion = kaartjes.strijdKaarten[currentCard]
    currentCard += 1
    return textForQuestion

def mousePressed():
    global pressed, timerOO
    if isMouseWithinSpace((600,200,200,50)) and pressed > 1:
        timerOO = True
        pressed = 1
    if isMouseWithinSpace((400,200,200,50)) and pressed > 1:
        #invoegen met hulp van jullie

def cardGevolg():
    x = random(1,4)
    ans ""

    if x = 1:
        ans = "plus 5 litpunten"
    if x = 2:
        ans = "min 5 litpunten"
    if x = 3:
        ans = "plus 5 carbonfootprint"
    if x = 4:
        ans = "min 5 carbonfootprint"

def givePlayerCard():
    
    playerinfo[name].Inventory = cardGevolg()
    page = "Menu"



#add to playerinfo:
#Inventory