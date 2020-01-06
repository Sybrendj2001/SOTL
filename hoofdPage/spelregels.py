import menu

def setup():
    global imgKans, imgStrijd, imgStop, imgCon, imgBack
    
    imgKans = loadImage("achterkant_kans2.jpeg")
    imgStrijd = loadImage("achterkant_strijd2.jpeg")
    imgStop = loadImage("stop.png")
    imgCon = loadImage("continue.png")
    imgBack = loadImage("back.png")
    
def draw(spelregel):
    global imgKans, imgStrijd, imgStop, imgCon, imgBack
    
    image(imgBack,width-150,50,100,100)
    
    textSize(18)
    
    if spelregel == 0:
        
        fill(255)
        
        textAlign(CENTER,CENTER)
        text("SPELDOEL\n",width/2-50,50,100,50)
        text("Er zijn 2 speldoelen omdat er ook 2 verschillende groepen zijn(woke en lit). De bedoeling van de lit mensen is om zo snel mogelijk bij de 75 punten te komen.De woke mensen proberen juist van 75 naar de 0 te komen.",width/2-375,100,750,100)
        
        
        
        image(imgKans,100,300,200,132)
        image(imgStrijd,100,452,200,132)
        image(imgCon,100,604,100,100)
        image(imgStop,100,724,100,100)
        
        textAlign(LEFT,TOP)
        text("Dit geeft kans/kenniskaarten weer.",450,366,650,40)
        text("Dit geeft strijdkaarten weer.",450,518,650,40)
        text("Dit zorgt ervoor dat de volgende speler aan de beurt komt als je geen kaart hoeft te pakken.",450,653,850,40)
        text("De stop knop zorgt ervoor dat je vervroegd stopt met het spel als je eerder klaar bent.",450,774,850,40)
    
    if spelregel == 1 or spelregel == 2:
        fill(255)
        textAlign(CENTER,TOP)
        text("Kanskaart:",100,200,600,40)
        text("Kenniskaart:",width-700,200,600,40)
        text("Als je een kanskaart krijgt, krijg je een verhaaltje. Ook staat er op het kaartje het aantal punten dat je kan krijgen. Soms zit er een kanskaart bij die vereist dat je een keuze moet maken of een dobbelsteen moet gooien. Klik dan op de keuze die je wil of op de dobbelsteen en klik dan op de terug knop.",100,250,600,200)
        text("Bij een kenniskaart moet je proberen het juiste antwoord te geven. Dit doe je door een vierkant aan te klikken waar het antwoord instaat waarvan jij denkt dat het goede antwoord erin staat. Je krijgt gelijk te zien of het goed of fout was(groene kleur betekent goed, rood betekent fout). Indien het antwoord fout was krijg je het goede antwoord ook te zien.",width-700,250,600,200)
        
        textAlign(CENTER,CENTER)
        image(imgBack,425,500,100,100)
        text("Dit is de terug knop. Met dit knopje ga je terug naar de hoofd pagina. Bij kaarten waar je keuze hoeft te maken zie je dit er gelijk bij staan. Bij de kaarten waar je een keuze moet maken komt deze knop te voorschijn nadat je een keuze hebt gemaakt.",575,500,600,100)
    
    
    if spelregel == 3:
        
        
        
        fill(255)
        rect(100,350,200,50)
        textSize(25)
        text("Start Timer", 175, 300)
        
        fill(255)
        rect(100,475,200,50)
        text("Assign", 175, 425)
        
        textAlign(LEFT,CENTER)
        text("Als je op de witte rechthoek onder Start Timer klikt dan gaat er een timer lopen van 30 secondes. wanneer de 30 secondes zijn afgelopen zal je dit op het scherm zien",450,300,650,100)
        text("Als je op de witte rechthoek onder Assign klikt dan krijg je een pop-up scherm met de vraag om het aan iemand te assignen. Hier vul je de speler die de strijd kaart heeft gewonnen.",450,425,650,100)
        
    
def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False


def mousePressed(spelregel):
    
    page = "spelregels"
    
    if isMouseWithinSpace(width-150,50,100,100) and spelregel == 0:
        page = "menu"
    
    if isMouseWithinSpace(width-150,50,100,100) and spelregel == 1:
        page = "kaarten"
        
    if isMouseWithinSpace(width-150,50,100,100) and spelregel == 2:
        page = "antwoorden"
    
    if isMouseWithinSpace(width-150,50,100,100) and spelregel == 3:
        page = "strijd"
        
    return page
        
    
