import menu

def draw(mode):
    fill(255)
    
    textAlign(CENTER,CENTER)
    text("SPELDOEL\n",width/2-50,50,100,50)
    text("Er zijn 2 speldoelen omdat er ook 2 verschillende groepen zijn(woke en lit). De bedoeling van de lit mensen is om zo snel mogelijk bij de 75 punten te komen.De woke mensen proberen juist van 75 naar de 0 te komen.",width/2-375,100,750,100)
    
    imgKans = loadImage("achterkant_kans2.jpeg")
    imgStrijd = loadImage("achterkant_strijd2.jpeg")
    imgStop = loadImage("stop.png")
    imgCon = loadImage("continue.png")
    
    image(imgKans,100,300,200,132)
    image(imgStrijd,100,452,200,132)
    image(imgCon,100,604,100,100)
    image(imgStop,100,724,100,100)
    
    textAlign(LEFT,TOP)
    text("Dit geeft kans/kenniskaarten weer.",500,366,650,40)
    text("Dit geeft strijdkaarten weer.",500,518,650,40)
    text("Dit zorgt ervoor dat de volgende speler aan de beurt komt als je geen kaart hoeft te pakken.",500,653,850,40)
    text("De stop knop zorgt ervoor dat je vervroegd stopt met het spel als je eerder klaar bent.",500,774,850,40)

       
    
