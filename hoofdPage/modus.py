def draw():
    global m, font
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
    
    if isMouseWithinSpace((width/4)-75, (height/2)-60,150,150):
        mode = "volledige versie"
        page = "menu"
        return page,mode
    
    elif isMouseWithinSpace((width*3/4)-75, (height/2)-60,150,150):
        mode = "verkorte versie"
        page = "menu"
        return page,mode
    
    return page, mode
