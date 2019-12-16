import menu

def draw(mode):
    fill(0)
    menu.draw(mode)
    textAlign(LEFT,CENTER)
    text("<- dobbelstenen:\n Klik hierop om de dobbelstenen te rollen",260,100)
    text("<- kans/kenniskaart: Klik hierop om een kans/kenniskaart te trekken",260,325)
    text("<- strijdkaart: Klik hierop om een strijdkaart te trekken",260,150)
    text("<- skip beurt: Klik hierop als je geen kaart hoeft te trekken",210,504)
    text("stop knop: dit stop het spel vroegtijdig en je komt dan bij de eind pagina ->",width-440,85)
    
    
