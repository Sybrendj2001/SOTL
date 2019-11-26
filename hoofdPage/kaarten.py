def setup(vraag):
    global kenniskaarten, r1, g1, b1, r2, r3, r4, r5, b2, b3, b4, b5, g2, g3, g4, g5, v, pressed
    
    r1 = 255
    g1 = 255
    b1 = 255
    
    r2 = 255
    g2 = 255
    b2 = 255
    
    r3 = 255
    g3 = 255
    b3 = 255
    
    r4 = 255
    g4 = 255
    b4 = 255
    
    r5 = 255
    g5 = 255
    b5 = 255
    
    pressed = 0
    
    v = vraag
    

    
    kenniskaarten = [["Welk jaar was het warmst in de tijd dat wij op aarde leven en het weer konden meten (1880)?","A = 2018","B = 2016","C = 2010","D = 2006","B"],
                     ["Welke 3 landen doen het meest aan milieuvriendelijkheid?","A = oostenrijk, zwitserland, denemarken","B = frankrijk, oostenrijk, zwitserland", "C = zwitserland, frankrijk, denemarken","D = frankrijk, zwitserland, denemarken","D"],
                     ["Waarom doet frankrijk het zo goed qua milieuvriendelijkheid?","A = ontzettend veel vegetariers","B = kluizenaars","C = subsidies voor milieuvriendelijke projecten", "D = water controlering","C"],
                     ["Waarom geven mensen elkaar de schuld qua plastic vervuiling?","A = omdat er niet gerecycled wordt","B = vanwege het onnodige/overmatige gebruik van plastic","C = omdat er te weinig prullenbakken zijn om hun vuil weg te gooien","D = de chinezen produceren te veel plastic","E = alle antwoorden zijn enigszins juist","E"],
                     ["Wat is de voornaamste redenen dat mensen tegen je zeggen dat je hypocriet bezig bent als je een verandering maakt in je gedrag en leefgedrag?","A = principiele keuzes zijn moeilijk te verdragen, omdat mensen om je heen weten dat je beter bezig bent dan zij zijn","B = ze geloven niet in verandering","C = we zijn gewoon gekkies","A"],
                     ["Als je moest kiezen tussen nooit meer roken of nooit meer seks, wat is dan slechter voor je?","A = sex, want je krijgt vaker problemen met de condoom dan met je sigaret","B = roken, want er wordt een gratis actie gehouden door de spar om gratis condooms weg te geven ipv sigaretten kopen","C = roken natuurlijk, beter gewoon seks","D = seks, want je bent misschien aseksueel","C"],
                     ["Wat heeft meer impact op het milieu, een heel jaar vlees eten (elke dag) of elke dag nieuwe spullen (gebruiksgoederen) kopen?","A = heel jaar t-bone steak eten en met dessert een ragout","B = heel jaar kip eten","C = elke dag de hema leegkopen","D = teveel troep kopen elke dag en vlees beperkt","D"],
                     ["Welke lamp wordt hoog aangeprezen voor het verminderen van energie, maar is qua duurzaamheid niet de beste optie?","A = een bouwlamp","B = lichtgenerator auto","C = led lamp (tl buizen)","D = de spaarlamp","D"],
                     ["Wat kan een reden zijn voor een overheid om niet te subsidieren?","A = ze hebben het geld niet","B = er kan/wil geen geld in onderzoeken worden gestopt om een business te controleren op milieuvriendelijkheid","C = bedrijven maken processen te complex en zijn weer afhankelijk van andere bedrijven om hun proces op orde te houden","D = antwoorden zijn onjuist","D"],
                     ["Wat doen wij als Nederlanders erg goed qua milieuvriendelijkheid en waar staan wij ook erg bekend om?","A = plastic verzamelen en recyclen","B = watermanagement","C = fietsen","D = alle antwoorden zijn  juist","D"],
                     ["Hoeveel landen tekenden het klimaatakkoord in Parijs in 2016?","A = ca. 100 landen","B = 50 landen","C = ca. 20 landen","D= ca. 190 landen","D"],
                     ["Hoeveel procent van alle klimaatwetenschappers stellen dat de mens de oorzaak is van de klimaatverandering?","A = 67%","B = 42%","C = 86%","D = 97%","D"],
                     ["Wie zijn nog meer slachtoffer van een nood ramp die plaatsvindt, door het gevolg van klimaatverandering?","A = bedrijven","B = dieren","C = de aarde","B"],
                     ["Welk land is de grootse investeerder in hernieuwbare energie?","A = Amerika","B = China","C = Rusland","B"],
                     ["Welke reden geldt niet meer als een voorname oorzaak als mensen hun land verlaten/uitvluchten?","A = oorlog","B = geld","C = klimaat","B"],
                     ["Wat is een andere gassoort die zorgt voor klimaatopwarming en is ook afkomstig van de scheten van koeien en schapen?","A = co2","B = methaan","C = lachgas","B"],
                     ["Hoeveel ton C02 wordt er gemiddeld door een gezin per jaar uitgestoten?","A = 2 ton","B = 15 ton","C = 23 ton","C"],
                     ["Op welke hoogte ligt onze atmosfeer?","A = 10.000 meter","B = 8.000 meter","C = 5.000 meter","D= 15.000 meter","A"],
                     ["Wat is een verrassende feit als je thuis bewust wilt zijn van je footprint?","A = minder tv kijken","B = wassen met kouder water","C = minder roken thuis","B"],
                     ["Wat is handig om thuis te vervangen, je wasdroger of je (nog) werkende koelkast?","A = je wasdroger, verkoop hem en koop een wasrek (bespaart geld)!","B = je werkende koelkast","C = beide antwoorden zijn juist","C"],
                     ["Welk merk bracht als eerste een elektrische auto uit?","A = Volkswagen","B = Porsche","C = Tesla","D = Ford","B"],
                     ["Welk dier is per kilo vlees het meest klimaatonvriendelijk om te eten?","A = Koe","B = Varken","C = Kip","D = Eend","A"],
                     ["Welk land heeft per jaar de meeste toeristen?", "A = U.S.A.", "B = Spanje","C = Italie","D = Frankrijk","D"],
                     ["Wie van de mensen hieronder had meer instagram volgers aan het begin van 2019?","A = Beyonce","B = Ariana Grande","C = Kim Kardashian","D = Cristiano Ronaldo","D"],
                     ["Hoeveel procent van het oceaanplastic is microplastic? (<5mm)","A = 24%","B = 8%","C = 64%","D = 11%","B"],
                     ["Hoeveel soorten bijen waren er ooit in Nederland?","A = ca. 40","B = ca. 460","C = ca. 230","D = ca. 300","D"],
                     ["Het houden van honingbijen is niet goed voor het milieu?","A = Waar","B = Niet waar","B"],
                     ["Hoeveel mensen zouden er zonder armoede kunnen leven als iedereen veganist zou zijn?","A = 12,0 miljard","B = 7,5 miljard","C = 4,8 miljard","D = 6,95 miljard","B"],
                     ["Om een kilo rundvlees te laten groeien, heb je X liter water nodig. Wat is X?","A = 1500","B = 7500","C = 900","D = 15500","D"],
                     ["De NL overshoot day 2018 valt op:(Dit is de datum waarop de jaarlijkse vraag van de mensheid naar de natuur groter wordt dan wat de ecosystemen van de aarde in het hele jaar kunnen regenereren.)","A = 1 januari","B = 1 augustus","C = 21 oktober","D = 1 juni"],
                     ["Het voedsel voor het vee van NL komt voornamelijk uit:","A = Het gekapte regenwoud in de Amazone","B = Kassen in de woestijn","C = Kassen in Nederland","D = Europa","A"],
                     ["Een pescetarier is iemand die:","A = <1 jaar veganist is","B = geen dieren eet, behalve insecten","C = geen dieren eet, behalve vis","D = alleen planten en schimmels eet","C"],
                     ["Welke gemeenschap is het kwetsbaarst voor hevige hitte?","A = Het platteland","B = De stad","C = De buitenwijken van een stad","D = Ongecontacteerde inheemse culturen","B"],
                     ["Hoeveel meter stijgt de zeespiegel, wanneer al het landijs smelt?","A = 4","B = 7","C = 12","D = 10","D"],
                     ["Hoe hoog/laag ligt Rotterdam t.o.v. de zeespiegel?","A = +1m","B = -4m","C = -6m","D = + 2m","A"],
                     ["Hoe veroorzaakt extreem weer mentale stoornissen?","A = Overproductie van serotonine door hitte","B = Verhoogde druk op de hersenen","C = Verhoogde seizoensdepressie","D = PTSS","D"],
                     ["46 % van het plastic in zee, bestaat uit:","A = visnetten","B = wegwerpplastic","C = microplastics zoals vezels van kleding","D = Industrieel afval","A"],
                     ["Wat is het meest voorkomende broeikasgas in de atmosfeer?","A = Methaan","B = Chloorfluorkoolwaterstoffen","C = Waterdamp","D = CO2","E = N2","B"],
                     ["Sinds 1880 tot 2020 is de wereldwijde temperatuur:","A = 2,0 gestegen","B = 1,7 gestegen","B = 1,7 gestegen","D = 3,4 gestegen","B"],
                     ["Hoeveel procent van alle rifgroeiende koralen is bedreigd?","A = 78%","B = 44%","C = 27%","D = 33%","D"],
                     ["Van 1 April 2018-1 April 2019 is de wereldwijde bijenpopulatie","A = 7% gedaald", "B = 14% gedaald","C = 21% gedaald","D = 41% gedaald","D"],
                     ["Wat is het geschatte jaar, waarin zich meer plastic, dan vissen in de zee bevindt?","A = 2060","B = 2048","C = 2026","D = 2030","B"],
                     ["Eend, een van de productiefste vormen van vleesproductie, heeft een rendement van:","A = 40/1 kg voer naar vlees","B = 7/1 kg voer naar vlees","C = 36/1 kg voer naar vlees","D = 10/1 kg voer naar vlees","C"],
                     ["Van al het verbouwde voedsel wordt x% verspild","A = 33","B = 50","C = 21","D = 64","A"],
                     ["Welk broeikasgas is het krachtigst?","A = Methaan","B = Waterstof","C = N2O","D = CO2","A"],
                     ["Overleven bacterien en virussen tientallen tot honderden jaren in permafrost?","A = Ja","B = Nee","A"],
                     ["Klimaatverandering zorgt ervoor dat sommige soorten zich verspreiden. Zoals de tijgermug. Deze veroorzaakt:","A = Chikungunya","B = Dengue/knokkelkoorts","C = Gele koorts","D = Zika","E = Allemaal","E"]]
    
    
    
def draw():
    global kenniskaarten, r1, g1, b1, r2, r3, r4, r5, b2, b3, b4, b5, g2, g3, g4, g5, v
    
    
    background(255)
    fill(0)
    textAlign(CENTER,CENTER)
    text(str(kenniskaarten[v][0]),100,50,450,75)
    
    if len(kenniskaarten[v]) == 7:
        
        fill(r1, g1, b1)
        rect(100,150,450,40)
        fill(r2,g2,b2)
        rect(100,200,450,40)
        fill(r3,g3,b3)
        rect(100,250,450,40)
        fill(r4,g4,b4)
        rect(100,300,450,40)
        fill(r5,g5,b5)
        rect(100,350,450,40)
        
        fill(0)
        text(str(kenniskaarten[v][1]),100,150,450,40)
        text(str(kenniskaarten[v][2]),100,200,450,40)
        text(str(kenniskaarten[v][3]),100,250,450,40)
        text(str(kenniskaarten[v][4]),100,300,450,40)
        text(str(kenniskaarten[v][5]),100,350,450,40)
    
    if len(kenniskaarten[v]) == 6:
        
        fill(r1, g1, b1)
        rect(100,150,450,40)
        fill(r2,g2,b2)
        rect(100,200,450,40)
        fill(r3,g3,b3)
        rect(100,250,450,40)
        fill(r4,g4,b4)
        rect(100,300,450,40)
        
        fill(0)
        text(str(kenniskaarten[v][1]),100,150,450,40)
        text(str(kenniskaarten[v][2]),100,200,450,40)
        text(str(kenniskaarten[v][3]),100,250,450,40)
        text(str(kenniskaarten[v][4]),100,300,450,40)
    
    if len(kenniskaarten[v]) == 5:
        
        fill(r1, g1, b1)
        rect(100,150,450,40)
        fill(r2,g2,b2)
        rect(100,200,450,40)
        fill(r3,g3,b3)
        rect(100,250,450,40)
        
        fill(0)
        text(str(kenniskaarten[v][1]),100,150,450,40)
        text(str(kenniskaarten[v][2]),100,200,450,40)
        text(str(kenniskaarten[v][3]),100,250,450,40)
    
    if len(kenniskaarten[v]) == 4:
        
        fill(r1, g1, b1)
        rect(100,150,450,40)
        fill(r2,g2,b2)
        rect(100,200,450,40)
        
        fill(0)
        text(str(kenniskaarten[v][1]),100,150,450,40)
        text(str(kenniskaarten[v][2]),100,200,450,40)


    

def randomKaart():
    
    kkKaart = int(random(0,46))
    
    return kkKaart


def isMouseWithinSpace(x,y,w,h):
    if (x < mouseX < x + w and y < mouseY < y + h):
        return True
    else:
        return False

def mousePressed():
    global kenniskaarten, r1, g1, b1, r2, r3, r4, r5, b2, b3, b4, b5, g2, g3, g4, g5, v, pressed
    
    
    a = kenniskaarten[v][len(kenniskaarten[v])-1] + " ="
    
    if isMouseWithinSpace(100,150,450,40) and pressed < 1:
        if a in kenniskaarten[v][1]:
            r1 = 30
            g1 = 237
            b1 = 26
            pressed = pressed + 1
            return "right"
        
        else:
            r1 = 255
            g1 = 97
            b1 = 97
            pressed = pressed + 1
            return "wrong"

    elif isMouseWithinSpace(100,200,450,40) and pressed < 1:
        if a in kenniskaarten[v][2]:
            r2 = 30
            g2 = 237
            b2 = 26
            pressed = pressed + 1
            return "right"
        
        else:
            r2 = 255
            g2 = 97
            b2 = 97
            pressed = pressed + 1
            return "wrong"

    elif isMouseWithinSpace(100,250,450,40) and len(kenniskaarten[v]) > 4 and pressed < 1:
        if a in kenniskaarten[v][3]:
            r3 = 30
            g3 = 237
            b3 = 26
            pressed = pressed + 1
            return "right"
        
        else:
            r3 = 255
            g3 = 97
            b3 = 97
            pressed = pressed + 1
            return "wrong"

    elif isMouseWithinSpace(100,300,450,40) and len(kenniskaarten[v]) > 5 and pressed < 1:
        if a in kenniskaarten[v][4]:
            r4 = 30
            g4 = 237
            b4 = 26
            pressed = pressed + 1
            return "right"
        
        else:
            r4 = 255
            g4 = 97
            b4 = 97
            pressed = pressed + 1
            return "wrong"
        
    elif isMouseWithinSpace(100,350,450,40) and len(kenniskaarten[v]) > 6 and pressed < 1:
        if a in kenniskaarten[v][4]:
            r5 = 30
            g5 = 237
            b5 = 26
            pressed = pressed + 1
            return "right"
        
        else:
            r5 = 255
            g5 = 97
            b5 = 97
            pressed = pressed + 1
            return "wrong"
    return "niets"
