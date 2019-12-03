import kaarten, kaartjes, personInfo

def draw(ant):
    
    kaarten.draw()
    
    text("you pressed the "+ ant +" anwser!",width/2-50,600)
    
    fill(255)
    rect(600,100,100,100)
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False
    
    
def mousePressed(ant):
    page = "antwoorden"
    
    
    if isMouseWithinSpace(600,100,100,100):
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
