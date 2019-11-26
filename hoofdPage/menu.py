import personInfo

    
def draw():
    

    
    i = 0
    
    textAlign(LEFT,CENTER)
    

    
    fill(255)
    background(255)
    rect(499,199,202,134)
    rect(499,449,202,134)
    
    fill(255)
    
    s = 150
    q = 170
    
    while  i < len(personInfo.playerList):
        n = personInfo.playerList[i].name
        
        if personInfo.playerList[i].role == "woke":
            p = personInfo.playerList[i].wokeScore
        else:
            p = personInfo.playerList[i].litScore
            
        fill(0)
        text("player" + str(i+1) + ": " + n,60,s,190,40)
        text(str(p),60,q,190,40)
        
        q = q + 50
        s = s + 50
        i += 1
        
    
