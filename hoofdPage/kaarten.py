import kaartjes, personInfo, random

def setup():
    global r1, g1, b1, r2, r3, r4, r5, b2, b3, b4, b5, g2, g3, g4, g5, pressed, imgBack, kans, imgKans, imgBook, dobbel
    
    dobbel = 1
    
    r1 = 255
    g1 = 255
    b1 = 255
    
    r2 = 255
    g2 = 255
    b2 = 255
    
    r3 = 255
    g3 = 255
    b3 = 255
    
    r4 = 255
    g4 = 255
    b4 = 255
    
    r5 = 255
    g5 = 255
    b5 = 255
    
    pressed = 0
    
    imgBack = loadImage("back.png")
    kans = loadImage("kans.jpeg")
    imgKans = loadImage("achterkant_kans2.jpeg")
    imgBook = loadImage("book1.png")
    
def draw():
    global r1, g1, b1, r2, r3, r4, r5, b2, b3, b4, b5, g2, g3, g4, g5, imgBack, kans, imgKans, imgBook, dobbel
    
    textAlign(CENTER,CENTER)
    
    
    fill(255)
    rect(39,149,202,134)
    
    image(kans,width/2-400,height/2-264,800,528)
    image(imgKans,40,150,200,132)
    image(imgBook,40,height-150,100,120)
    
    textSize(37)
    text("SURVIVAL OR THE LITTEST\nMENU",(width/2)-250,0,500,150)
    textSize(14)
    
    if kaartjes.kansEnKennis[0] in kaartjes.kenniskaarten:
        fill(0)
        text(kaartjes.kansEnKennis[0][0],width/2-225,250,450,75)
            
        fill(r1, g1, b1)
        rect(width/2-225,350,450,40)
        fill(r2,g2,b2)
        rect(width/2-225,400,450,40)
            
        if len(kaartjes.kansEnKennis[0]) > 4:
            fill(r3,g3,b3)
            rect(width/2-225,450,450,40)
            
        if len(kaartjes.kansEnKennis[0]) > 5:
            fill(r4,g4,b4)
            rect(width/2-225,500,450,40)
            
        if len(kaartjes.kansEnKennis[0]) > 6:
            fill(r5,g5,b5)
            rect(width/2-225,550,450,40)
        
        
        i = 1
        h = 350
        while i < (len(kaartjes.kansEnKennis[0])-1):
            fill(0)
            textSize(10)
            text(str(kaartjes.kansEnKennis[0][i]),width/2-225,h,445,40)
            h = h + 50
            i = i + 1
        
        
    
    if kaartjes.kansEnKennis[0] in kaartjes.kanskaarten:
        fill(0)
        image(imgBack,1250,186,100,100)
        
        text(str(kaartjes.kansEnKennis[0][0]),width/2-225,height/2-75,450,150)
        
        text("Carbon footprint:\n" + str(kaartjes.kansEnKennis[0][1]),width/2-350,height/2+180,120,40)
        text("litpunten:\n" + str(kaartjes.kansEnKennis[0][2]),width/2+280,height/2+180,80,40)
    
    if kaartjes.kansEnKennis[0] in kaartjes.kansSpeciaal:
        if len(kaartjes.kansEnKennis[0]) < 4:
            
            j = 1
            while j < 7:
                if j == dobbel:
                    dice = loadImage("dice" + str(j) + ".png")
                j += 1
            
            image(dice,width/2-50,500,100,100)
            rect(width/2-50,500,100,100)
            fill(255)
            
            fill(0)
            text(kaartjes.kansEnKennis[0][0],width/2-225,height/2-75,450,150)
            
            if pressed == 1 and dobbel % 2 == 0:
                text("Carbon footprint:\n" + str(kaartjes.kansEnKennis[0][1][0]),width/2-350,height/2+180,120,40)
                text("litpunten:\n" + str(kaartjes.kansEnKennis[0][1][1]),width/2+280,height/2+180,80,40)
                image(imgBack,1250,186,100,100)
                
            elif pressed == 1:
                text("Carbon footprint:\n" + str(kaartjes.kansEnKennis[0][2][0]),width/2-350,height/2+180,120,40)
                text("litpunten:\n" + str(kaartjes.kansEnKennis[0][2][1]),width/2+280,height/2+180,80,40)
                image(imgBack,1250,186,100,100)
                
        else:
            fill(0)
            text(str(kaartjes.kansEnKennis[0][0]),width/2-225,350,450,40)
            
            fill(255)
            rect(width/2-225,450,450,40)
            fill(0)
            text(kaartjes.kansEnKennis[0][1],width/2-225,450,450,40)
            
            fill(255)
            rect(width/2-225,500,450,40)
            fill(0)
            text(kaartjes.kansEnKennis[0][2],width/2-225,500,450,40)
        
            text("Carbon footprint:\n" + "A = " + str(kaartjes.kansEnKennis[0][3][0]) + " or B = " +str(kaartjes.kansEnKennis[0][4][0]),width/2-350,height/2+180,120,40)
            text("litpunten:\n" + "A = " + str(kaartjes.kansEnKennis[0][3][1]) + " or B = " +str(kaartjes.kansEnKennis[0][4][1]),width/2+230,height/2+180,120,40)
            
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    


    
def mousePressed():
    global r1, g1, b1, r2, r3, r4, r5, b2, b3, b4, b5, g2, g3, g4, g5, pressed, dobbel
    
    page = "kaarten"
    ant = "niets"
    
    if isMouseWithinSpace(40,height-150,100,120):
        page = "spelregels"
    
    if kaartjes.kansEnKennis[0] in kaartjes.kenniskaarten:
        
        a = kaartjes.kansEnKennis[0][-1] + " ="
        
        if isMouseWithinSpace(width/2-225,350,450,40) and pressed < 1:
            pressed = pressed + 1
            if a in kaartjes.kansEnKennis[0][1]:
                r1 = 30
                g1 = 237
                b1 = 26
                ant = "right"
            else:
                r1 = 255
                g1 = 97
                b1 = 97
                ant = "wrong"
        
        if isMouseWithinSpace(width/2-225,400,450,40) and pressed < 1:
            pressed = pressed + 1
            if a in kaartjes.kansEnKennis[0][2]:
                r2 = 30
                g2 = 237
                b2 = 26
                ant = "right"
            else:
                r2 = 255
                g2 = 97
                b2 = 97
                ant = "wrong"
       
        if isMouseWithinSpace(width/2-225,450,450,40) and pressed < 1 and len(kaartjes.kansEnKennis[0]) > 4:
            pressed = pressed + 1
            if a in kaartjes.kansEnKennis[0][3]:
                r3 = 30
                g3 = 237
                b3 = 26
                ant = "right"
            else:
                r3 = 255
                g3 = 97
                b3 = 97
                ant = "wrong"
                
                
        if isMouseWithinSpace(width/2-225,500,450,40) and pressed < 1 and len(kaartjes.kansEnKennis[0]) > 5:
            pressed = pressed + 1
            if a in kaartjes.kansEnKennis[0][4]:
                r4 = 30
                g4 = 237
                b4 = 26
                ant = "right"
            else:
                r4 = 255
                g4 = 97
                b4 = 97
                ant = "wrong"
                
        if isMouseWithinSpace(width/2-225,550,450,40) and pressed < 1 and len(kaartjes.kansEnKennis[0]) > 6:
            pressed = pressed + 1
            if a in kaartjes.kansEnKennis[0][5]:
                r5 = 30
                g5 = 237
                b5 = 26
                ant = "right"
            else:
                r5 = 255
                g5 = 97
                b5 = 97
                ant = "wrong"
                
        
        
        
    if kaartjes.kansEnKennis[0] in kaartjes.kanskaarten:
        if isMouseWithinSpace(1250,186,100,100):
            
            page = "menu"
            
            if personInfo.currentPlayer.role == "woke":
                personInfo.scoreChange(personInfo.currentPlayer,"woke",kaartjes.kansEnKennis[0][1])
            else:
                personInfo.scoreChange(personInfo.currentPlayer,"lit",kaartjes.kansEnKennis[0][2])
                
            l = kaartjes.kansEnKennis[0]
    
            kaartjes.kansEnKennis.append(l)
            kaartjes.kansEnKennis.remove(kaartjes.kansEnKennis[0])
            
            personInfo.turnIncrement()
        
    if ant != "niets":
        page = "antwoorden"
        
    if kaartjes.kansEnKennis[0] in kaartjes.kansSpeciaal:
        if len(kaartjes.kansEnKennis[0]) < 4:
            if isMouseWithinSpace(width/2-50,500,100,100) and pressed < 1:
                pressed += 1
                dice()
            
            if isMouseWithinSpace(1250,186,100,100) and pressed == 1:
                
                if dobbel % 2 == 0:
                    if personInfo.currentPlayer.role == "woke":
                        personInfo.scoreChange(personInfo.currentPlayer,"woke",kaartjes.kansEnKennis[0][1][0])
                    else:
                        personInfo.scoreChange(personInfo.currentPlayer,"lit",kaartjes.kansEnKennis[0][1][1])
                        
                else:
                    if personInfo.currentPlayer.role == "woke":
                        personInfo.scoreChange(personInfo.currentPlayer,"woke",kaartjes.kansEnKennis[0][2][0])
                    else:
                        personInfo.scoreChange(personInfo.currentPlayer,"lit",kaartjes.kansEnKennis[0][2][1])
                
                
                l = kaartjes.kansEnKennis[0]
    
                kaartjes.kansEnKennis.append(l)
                kaartjes.kansEnKennis.remove(kaartjes.kansEnKennis[0])
            
                personInfo.turnIncrement()
                
                page = "menu"
        
        else:
            if isMouseWithinSpace(width/2-225,450,450,40):
                if personInfo.currentPlayer.role == "woke":
                    personInfo.scoreChange(personInfo.currentPlayer,"woke",kaartjes.kansEnKennis[0][3][0])
                else:
                    personInfo.scoreChange(personInfo.currentPlayer,"lit",kaartjes.kansEnKennis[0][3][1])
                    
                l = kaartjes.kansEnKennis[0]
    
                kaartjes.kansEnKennis.append(l)
                kaartjes.kansEnKennis.remove(kaartjes.kansEnKennis[0])
            
                personInfo.turnIncrement()
                
                page = "menu"
            
            if isMouseWithinSpace(width/2-225,500,450,40):
                if personInfo.currentPlayer.role == "woke":
                    personInfo.scoreChange(personInfo.currentPlayer,"woke",kaartjes.kansEnKennis[0][4][0])
                else:
                    personInfo.scoreChange(personInfo.currentPlayer,"lit",kaartjes.kansEnKennis[0][4][1])
                
                l = kaartjes.kansEnKennis[0]
    
                kaartjes.kansEnKennis.append(l)
                kaartjes.kansEnKennis.remove(kaartjes.kansEnKennis[0])
            
                personInfo.turnIncrement()
                
                page = "menu"
                
        
    return page, ant


def dice():
    global dobbel
    
    dobbel = random.randint(1,6)
