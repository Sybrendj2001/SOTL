def draw():
    #presettings
    fill(245, 19, 19)
    textSize(25)
    
    #Button full game
    text("Play the full game", 500, 550)
    rect(500, 600, 250, 50)
    
    text("Play the short game", 800, 550)
    rect(800, 600, 250, 50)
    
def isMouseWithinSpace(x, y, breedte, hoogte):
    if x < mouseX < x + breedte and y < mouseY < y + hoogte:
        return True
    else:
        return False
   
def mousePressed():
    global m, font, textfont, scene
    page = "modus"
    mode = None
    
    if isMouseWithinSpace(500,600,250,50):
        mode = "volledige versie"
        page = "menu"
        return page,mode
    
    elif isMouseWithinSpace(800,600,250,50):
        mode = "verkorte versie"
        page = "menu"
        return page,mode
    
    return page, mode
