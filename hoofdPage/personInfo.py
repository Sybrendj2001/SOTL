from random import shuffle

#maakt een player-object
class Player:
    #een player heeft drie waarden die bij initialisatie al worden bepaald: de naam en de twee soorten punten
    def __init__(self,name, litScore, wokeScore):
        #raad eens
        self.name = name
        #woke of niet-woke, wordt alleen door functies aangepast
        self.role = ""
        #litpunten
        self.litScore = litScore
        #wokepunten
        self.wokeScore = wokeScore

def scoreChange(player, typ, amount):
    """functie om punten op te tellen"""
    if typ == "lit":
        player.litScore += amount
    elif typ == "woke":
        player.wokeScore += amount
    #deze else is alleen nodig als de functie handmatig wordt aangeroepen
    else:
        print("that's not an option >:(")

def input(message=''):
    """deze totaal niet van het internet gestolen methode vervangt de vanilla input() methode omdat het dezelfde naam heeft; functie plaatst de input als bericht boven de textbox"""
    #gebruikt gekke java methods en libraries
    from javax.swing import JOptionPane
    #uiteindelijk geeft de method terug wat je in de textbox invult
    return JOptionPane.showInputDialog(frame, message)

def assignRoles():
    """voegt lit-rollen toe aan de list; hoeveelheid is de helft van de spelers, afgerond naar beneden"""
    global playerList
    roleList = []
    #de helft, afgerond naar beneden, is lit
    for i in range(len(playerList)//2):
        roleList.append("lit")
    #de rest is woke
    for i in range(len(playerList)//2, len(playerList)):
        roleList.append("woke")
    #debug
    print(roleList)
    #roept de shuffle-methode uit de random library aan om de volgorde van de rollenlijst te husselen
    shuffle(roleList)
    #debug
    print(roleList)
    #elke speler krijgt een van de nu in random volgorde geplaatste rollen toegewezen
    for i in range(len(playerList)):
        playerList[i].role = roleList[i]
        
def checkAmount(string):
    global playerList
    players = int(input(string))
    if players >= 2 and players <= 8:
        for i in range (players):
            #geef elke speler een id, naam, rol, en zet de score op 0
            playerList.append(Player(input("Player %i, type your name: "%(i+1)), 0, 0))
    else:
        checkAmount("The amount of players has to be at least 2 and at most 8.")
        

def setup():
    global playerList
    #stop alle spelers in een lijst
    #intern worden de spelers geidentificeerd met hun positie in de lijst: speler 1 is dus playerList[0]
    playerList = []
    #deze functie instantifieert de spelers en voegt ze toe aan een list
    checkAmount("How many players are there?")
    #alexa what does assign mean in dutch
    assignRoles()
    
def draw():
    global playerList
    
