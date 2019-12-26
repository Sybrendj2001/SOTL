import personInfo

def setup():
    global points, player, role
    
    if personInfo.playerList[0].role == "woke":
        points = personInfo.playerList[0].wokeScore 
    else:
        points = personInfo.playerList[0].litScore
    
    player = personInfo.playerList[0].name
    role = personInfo.playerList[0].role
    
def draw():
    global points, player, role
    
    textAlign(CENTER,TOP)
    textSize(50)    
    text(player + " heeft gewonnen!",width/2-400,300,800,200)
    textSize(40)
    text("met " + str(points) + " punten",width/2-400,370,800,200)



def champ():
    global points, player, role
    
    i = 1
    
    while i < len(personInfo.playerList):
        
        p = personInfo.playerList[i].name
        
        if personInfo.playerList[i].role == "woke":
            a = personInfo.playerList[i].wokeScore
            y = difference(a,75)
            
        if personInfo.playerList[i].role == "lit":
            a = personInfo.playerList[i].litScore
            y = difference(a,0)
        
        if role == "woke":
            x = difference(points,75)
        else:
            x = difference(points,0)
            
        if y > x:
            points = a
            player = p
        
        i += 1

def difference(a,b):
    
    if a >= b:
        result = a - b
    else:
        result = b - a
   
    return result
        
