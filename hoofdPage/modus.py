def draw():
    fill(0)
    text("Speel de volledige versie", 130, 350 , 130, 300)
    text("Speel de verkorte versie", 530, 350 , 130, 300)


def isMouseWithinSpace(x, y, breedte, hoogte):
    if x < mouseX < x + breedte and y < mouseY < y + hoogte:
        return True
    else:
        return False
   
   
   
def mousePressed():
    global m, font, textfont, scene
    page = "modus"
    mode = None
    
    if isMouseWithinSpace(125,340,150,150):
        mode = "volledige versie"
        page = "menu"
        return page,mode
    
    elif isMouseWithinSpace(225,340,150,150):
        mode = "verkorte versie"
        page = "menu"
        return page,mode
    
    return page, mode
