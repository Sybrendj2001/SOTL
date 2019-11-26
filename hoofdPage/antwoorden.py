import kaarten, personInfo

def draw(a):
    global ant1
    ant1 = a
    
    background(255)
    
    kaarten.draw()
    if a == "right":
        text("You gave the right anwser",100,400,450,40)
    elif a == "wrong":
        text("You gave the wrong anwser",100,400,450,40)
        
    rect(600,100,100,100)
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed(ant,vraag):
    page = "antwoorden"
    
    if isMouseWithinSpace(600,100,100,100):
        if ant == "right":
            personInfo.scoreChange(personInfo.playerList[0],personInfo.playerList[0].role,3)
            
        else:
            personInfo.scoreChange(personInfo.playerList[0],personInfo.playerList[0].role,-2)
        
        page= "menu"
        ant = "niets"
        
        kaarten.setup(vraag)
    
    return ant, page
