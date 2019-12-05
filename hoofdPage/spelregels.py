import menu

def draw(mode):
    fill(0)
    menu.draw(mode)
    textAlign(LEFT,CENTER)
    text("<- dobbelstenen:\n Klik hierop om de dobbelstenen te rollen",260,100)
    text("<- kans/kenniskaart: Klik hierop om een kans/kenniskaart te trekken",260,150)
    text("<- strijdkaart: Klik hierop om een strijdkaart te trekken",260,325)
    text("skip beurt: Klik hierop als je geen kaart hoeft te trekken",100,750)
    text("player1",100,250)
    text("player2",100,300)
    text("player3",100,350)
    text("player4",100,400)
    text("player5",100,450)
    text("player6",100,500)
    text("player7",100,550)
    text("player8",100,600)
    text("dit geeft weer welke versie jij hbt gekozen",100,650)
    text("stop knop: dit stop het spel vroegtijdig en je komt dan bij de eind pagina",100,700)
    
    
