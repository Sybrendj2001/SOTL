import personInfo

def draw(mode):
    
    i = 0
    
    textAlign(LEFT,CENTER)

    background(255)
    
    fill(255)
    
    rect(499,199,202,134)
    rect(499,449,202,134)
    
    imgKans = loadImage("achterkant_kans2.jpeg")
    imgStrijd = loadImage("achterkant_strijd2.jpeg")
    
    image(imgKans,500,200,200,132)
    image(imgStrijd,500,450,200,132)
    
    s = 150
    q = 170
    
    while  i < len(personInfo.playerList):
        n = personInfo.playerList[i].name
        
        if personInfo.playerList[i].role == "woke":
            p = personInfo.playerList[i].wokeScore
        else:
            p = personInfo.playerList[i].litScore
            
        fill(0)
        text("player " + str(i+1) + ": " + n,60,s,190,40)
        text(str(p),60,q,190,40)
        
        q = q + 50
        s = s + 50
        i += 1
        
    textAlign(RIGHT,CENTER)
    text(str(mode),width-210,0,200,50)
        

def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False


def mousePressed():
    
    page = "menu"
    
    if isMouseWithinSpace(499,199,202,134):
        page = "kaarten"
    
    return page
