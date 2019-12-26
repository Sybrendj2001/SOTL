import kaarten, kaartjes, personInfo

def draw(ant):
    
    kaarten.draw()
    
    a = kaartjes.kansEnKennis[0][-1]
    
    if ant == "wrong":
        text("Je hebt het verkeerde antwoord aangeklinkt! Het juiste antwoord is " + a,width/2-225,600,450,40)
    else:
        text("Je hebt het juiste antwoord aangeklikt!",width/2-225,600,450,40)
    
    imgBack = loadImage("back.png")
    image(imgBack,1250,186,100,100)
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    
    
def mousePressed(ant):
    page = "antwoorden"
    
    if isMouseWithinSpace(40,height-150,100,120):
        page = "spelregels"
    
    if isMouseWithinSpace(1250,186,100,100):
        if ant == "right":
            if personInfo.currentPlayer.role == "lit":
                personInfo.scoreChange(personInfo.currentPlayer,"lit",3)
            else:
                personInfo.scoreChange(personInfo.currentPlayer,"woke",-3)
        else:
            if personInfo.currentPlayer.role == "lit":
                personInfo.scoreChange(personInfo.currentPlayer,"lit",-2)
            else:
                personInfo.scoreChange(personInfo.currentPlayer,"woke",2)
        
        l = kaartjes.kansEnKennis[0]
        
        kaartjes.kansEnKennis.append(l)
        
        kaartjes.kansEnKennis.remove(kaartjes.kansEnKennis[0])
        
        page= "menu"
        ant = "niets"
        
        personInfo.turnIncrement()
        
        kaarten.setup()
    
    return ant, page
