from random import shuffle

def setup():
    global kenniskaarten, kanskaarten, kansSpeciaal, kansEnKennis
    
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
    
    kanskaarten = [["Je zet een compostbak in de tuin waar je je etensresten in gooit. De compostbak wordt al snel een broedplaats voor insecten, en eigenlijk blijf je er het liefste uit de buurt.",-3,-4],
    ["Je koopt een nieuwe douchekop en je bent niet meer uit de badkamer te krijgen.",5,2],
    ["Je stapt over op Groeneco.",-5,0],
    ["Je gaat met vakantie op fietstocht door Nederland.",-4,4],
    ["Je bent eindelijk vrij en besluit om een roadtrip te gaan maken. Je hebt een hele leuke tijd in de steden die je bezoekt! Maar je verbruikt wel liters benzine om er te komen.",7,5],
    ["Je besluit mee te doen met een vrijwilligersactie om nieuwe bomen te planten in dichtbij gelegen natuurgebied.",-5,-2],
    ["Je besluit dat de karpervijver in de achtertuin toch niks voor jou is en gooit de karpers die nog leven in de dichtstbijzijnde sloot.",5,-3],    
    ["Je hebt een rol afgeslagen voor een milieubewuste film en bent gaan acteren in een blockbuster.",2,5],
    ["Je betaalt je milieubelasting per ongeluk dubbel.",-5,-2],
    ["Je vertelt aan een kleuterklas dat ze hun leven kunnen beteren door koud te douchen. Ze luisteren allemaal naar jou.",-3,1],
    ["Je vergeet de kraan van je bad uit te zetten voordat je naar je werk gaat.",3,-2],
    ["Je opent een insectenrestaurant waar alleen maar biologische burgers worden verkocht.",4,1],
    ["Je springt in een eekhoornpak naar beneden van een hoge berg, iets wat je altijd al had willen doen. Weer iets van je bucketlist af! Helaas land je verkeerd en breek je je been. Hierdoor moet de traumaheli ingevlogen worden.",4,7],
    ["Je bent het gezicht van nieuwe klimaatplan en wordt een grote meme op het hele internet.",-4,-4],
    ["Je wint de loterij en spendeert al je geld aan het verbeteren van het openbaar vervoer.",-6,3],
    ["Je betaald om instagram-volgers te krijgen en vertelt al je vrienden dit ook te doen. De servers draaien overuren!!!",4,-3],
    ["Je vrienden nodigen je uit om een avondje een drankje te doen in de stad. Iedereen spreekt af om met het openbaar vervoer te gaan.",-2,2],
    ["Je vertelt trots tegen al je collega\'s dat je promotie hebt geboekt bij Shell en shared dit ook op je twitter.",5,2],
    ["Je vrienden nodigen je uit om een avondje een drankje te doen in de stad. Jij besluit niet te komen en een avond extra te gaan werken als pizzabezorger voor thuisbezorgd. Je vervuilt hierdoor heel de binnenstad omdat je te hard rijd om je dagelijkse fooi te halen.",3,-4],
    ["Je besluit je school te overtuigen het dagelijkse koffiedik als potgrond te laten gebruiken voor de moestuin op het dak. Meerdere scholen volgen.",-6,3],
    ["Je organiseert een reunie waarbij je alles prominent vegan maakt. Het eten is zo lekker, dat 2 mensen je recepten vragen en voortaan ook vegan worden.",-2,2],
    ["Je hebt te veel weekmakers binnen-gekregen toen je op je scoubidou-touwtjes kauwde als kind. Je bent helaas onvruchtbaar. Wel kan je nog plezier maken in je leven.",-4,4],
    ["Je bent de nieuwe president van Nederland en besluit dat we met z\'n allen van fossiele brandstoffen af moeten. Je laat 10 kerncentrales bouwen.",-7,-7],
    ["Je ziet een documentaire over het klimaat die je de kriebels geeft. Zodra je thuis bent, zet je je afwasmachine en koelkast op ECO.",-3,0],
    ["Je overtuigt je ouders om hun lelijke onkruidtuin om te spitten en er meerjarige fruitstruiken neer te zetten.",-3,3],
    ["Je besluit in je huis een plastic en een papieren tasje op te hangen om afval te scheiden.",-4,1],
    ["Je hebt ein-de-lijk een relatie en je doucht samen. Dit bespaart soms water ;)",-1,4],
    ["Je zet de standaard schermachtergrond op je werk en school op zwart.",-2,0],
    ["Je wordt vegan!",-3,-1],
    ["Je wordt vegetarier!",-3,0],
    ["Je wint een Tesla!",-4,6],
    ["Je besluit een handleiding voor dummies te schrijven om bijenhotels te maken. Je biedt deze gratis aan aan middelbare scholen.",-2,2],
    ["Je vindt biodegradable 3D-print plastic uit.",-2,1],
    ["Je komt erachter dat de grootste banken in Nederland, investeren in zeer vervuilende projecten. Je stapt over.",-2,0],
    ["Je stemt op een groene partij.",-2,0],
    ["Je koopt een metalen spork!",-1,-1],
    ["Je wast niets meer met de hand af, maar gebruikt een afwasmachine en bespaart water.",-2,0],
    ["Je gaat op wereldreis en laat als influencer zien hoe je met het OV de mooiste reizen kan maken.",-2,7],
    ["Je demonstreert voor het milieu door je, samen met je vrienden, vast te ketenen aan alle vliegvelden.",-1,-2],
    ["Je schrijft een kinderboek waardoor kinderen hun ouders leren manipuleren beter voor de aarde te zorgen!",-2,-2],
    ["Je ontdekt en verspreidt een plastic-etende bacterie. Geef hem een naam.",-4,5],
    ["Je gebruikt NOOIT meer plastic wegwerpartikelen als rietjes, bestek, wattenstaafjes en.. tandenborstels?",-2,-1],
    ["Je rookt en je gooit je peuken altijd op de grond.",2,0],
    ["Je wint een reis naar New York!",2,4],
    ["Je gebruikt herbiciden in je tuin, om het onkruid tegen te gaan.",3,0],
    ["Je bestelt een rasdier bij een fokker.",1,5],
    ["Je wied je onkruid.",1,0],
    ["Je koopt elk jaar een nieuwe iPhone.",2,4],
    ["Je scheidt je afval niet, omdat je gewoon te lui bent.",1,0],
    ["Je maakt kunstwerken met afval.",0,0],
    ["Gefeliciteerd! Een baby, oh wacht, twee..",4,-4],
    ["Je houdt van je binnenplanten, maar je vermoordt ze steeds en koopt dan nieuwe.",2,0],
    ["Je bent een babyboomer!",2,-3],
    ["Je gebruikt tampons in plaats van een softcup.",1,0],
    ["Je verzamelt fleecedekens en wast ze vaak. Jammer genoeg worden de vissen nu ook gewassen met de vezels van je fleecedekens die van plastic gemaakt zijn :(",2,0],
    ["Je eet vlees.",1,1],
    ["Het sojavoer wordt op de vers afgebrande Amazone verbouwd voor de ruftende koeien.",3,-4],
    ["Je bent single, dus je doucht met niemand. Nerd!",-1,-6],
    ["Je houdt wel van flesjes water meenemen in plaats van een bidon he?",2,0],
    ["Je eet elke dag te veel dierlijke producten en hebt last van je darmen. Hierdoor verbruik je per toiletbezoek 1 toiletrol.",2,-3],
    ["Je traint heel hard en eet veel om er lekker en stoer uit te zien.",4,4],
    ["Je richt een coole hipster tent in met van die kekke retro gloeilampen.",-5,3],
    ["Je verwarming is kapot, dus zet je het gasfornuis aan, totdat het warm is...",3,-3],
    ["Je koopt een trouwring voor je vriendin met een houtsoort exclusief inheems aan het Amazone-gebied.",2,3],
    ["Je rijdt met zachte banden.",2,-2],
    ["Je gaat verhuizen en je koopt alleen maar nieuwe meubels.",2,2],
    ["Je houdt niet zo van schoonmaken, dus gebruik je liever bleekwater. Natuurlijk maakt het je niet uit dat je de waterzuivering flora vermoordt!",2,0],
    ["Je besluit de gehele zomer naar de naturistencamping om de hoek te gaan. je hoeft helemaal zwembroek te kopen! Maar je komt er ook je leuke buurmeisje tegen ;^)",-2,-3],
    ["Oeps... Je rijdt een kat dood...",-1,-4]
    ]
    
    
    kansSpeciaal = [["Je neemt een kat in plaats van een kind. Gooi 1 dobbelsteen, even en oneven nummers hebben andere waardes",[-2,2],[2,-2]],
    ["Je bent rijk geworden met je werk Maak een keuze","Je doneert veel geld aan projecten om bossen te beschermen en opnieuw te bebossen.","Je koopt een extra huis en 2 sportauto\'s.",[-8,2],[-2,8]],
    ["Je hebt een prijs van 10.000 euro gewonnen! Maak een keuze:","Koop een vliegticket naar N-Z","Koop de komende 3 jaar alles biologisch en lokaal"],
    ["Je begint een restaurant. Kies:","Veganistisch restaurant","korean bbq restaurant",[-4,-1],[5,-7]]
    ]
    
    kansEnKennis = kanskaarten + kenniskaarten + kansSpeciaal
    
    """
    strijdKaarten = [["Daag 1 speler uit. Het de uitgedaagde speler schat hoeveel global warming-termen ze kunnen opnoemen. Het tweede team zegt of ze dit kunnen overtreffen. Als ze dat kunnen, proberen ze dat. Als dit ze lukt krijgt ieder 5 punten richting hun doel."]
    ["Daag 1 speler uit. Het de uitgedaagde speler schat hoeveel videos met meer dan 2,5 miljard views ze kunnen opnoemen. Het tweede team zegt of ze dit kunnen overtreffen. Als ze dat kunnen, proberen ze dat. Als dit ze lukt krijgt ieder 5 punten richting hun doel."]
    ["Daag 1 speler uit. Het de uitgedaagde speler schat hoeveel instagram-accounts met meer dan 75 miljoen volgers ze kunnen opnoemen. Het tweede team zegt of ze dit kunnen overtreffen. Als ze dat kunnen, proberen ze dat. Als dit ze lukt krijgt ieder 5 punten richting hun doel."]
    ["Daag 1 speler uit. Het de uitgedaagde speler schat hoeveel landen in de top 20 koolstofemissie-landen ze kunnen opnoemen. Het tweede team zegt of ze dit kunnen overtreffen. Als ze dat kunnen, proberen ze dat. Als dit ze lukt krijgt ieder 5 punten richting hun doel."]
    ["Daag 1 speler uit. Het de uitgedaagde speler schat hoeveel woorden met meer dan 15 letters ze kunnen opnoemen. Het tweede team zegt of ze dit kunnen overtreffen. Als ze dat kunnen, proberen ze dat. Als dit ze lukt krijgt ieder 5 punten richting hun doel."]
    ["Degene die deze kaart trekt daagt iemand anders uit om te kijken wie er langer op 1 been kan staan. De winnaar krijgt 3 punten richting zijn/haar doel."]
    ["Speel steen papier schaar tegen een speler naar keuze. Degene die als eerste 2x wint steelt 3 punten naar keuze van de tegenstander."]
    ["Alle spelers noemen omstebeurt een bedreigde diersoort op. Wie als eerste niks meer weet moet alle andere spelers een punt richting hun doel geven."]
    ["De speler begint met het benoemen van een dier. Hierna bedenkt de volgende speler een dier dat begint met de laatste letter van het vorige dier. Wie als eerste niks meer weet geeft alle andere spelers een punt richting hun doel."]
    ["De speler begint met het benoemen van een land. Hierna bedenkt de volgende speler een land dat begint met de laatste letter van het vorige land. Wie als eerste niks meer weet geeft alle andere spelers een punt richting hun doel."]
    ["De speler begint met het benoemen van een automerk. Hierna bedenkt de volgende speler een automerk. Wie als eerste niks meer weet geeft alle andere spelers een punt richting hun doel."]
    ["De speler begint met het benoemen van een Nederlandse stad. Hierna bedenkt de volgende speler een stad die begint met de laatste letter van de vorige stad. Wie als eerste niks meer weet geeft alle andere spelers een punt richting hun doel."]
    ["De speler die deze kaart trekt moet vanaf nu alles met 1 hand doen. Als ze dit vergeten te doen moeten zij 5 punten van hun doel afstaan."]
    ["Speel een potje duim worstelen tegen de speler die het verste van zijn doel af is. Als je wint verdien je 1 punt richting jouw doel, als hij/zij wint krijgt hij/zij 2 punten."]
    ["Je mag een willekeurige speler uitkiezen die nu een kanskaart moet trekken."]
    ["Een speler naar keuze verliest 3 punten richting zijn/haar doel"]
    ["Bedenk in 30 seconden minstens 10 groenten. Als dit lukt krijg je 3 punten richting je doel."]
    ["Bedenk in 1 minuut minstens 10 jongensnamen. Als dit lukt krijg je 10 punten richting je doel."]
    ["Verdeel in 2 teams. Ieder team krijgt 30 sec om een top 3 te vormen over wat in nederland de meeste uitstoot veroorzaakt."]
    ["Speel met al je medespelers “Ik ga protesteren op Malieveld en ik neem mee”; een variatie op “ik ga op reis en ik neem mee” waar je manieren noemt om duurzamer te leven. De winnaar krijgt 10 punten naar zijn/haar doel."]
    ["Zet tussen 2 en 5 punten naar jouw doel in, kies voor even of oneven getallen en gooi met een dobbelsteen. Als je de juiste soort gooit, worden je punten verdubbeld; anders ben je ze kwijt."]
    ]
    """
    
    shuffle(strijdKaarten)
    shuffle(kansEnKennis)
