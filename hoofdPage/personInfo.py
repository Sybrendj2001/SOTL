from random import shuffle

#makes a player-object
class Player:
    #a player has three values which are determined by initialisation: the name and both types of points
    def __init__(self,name, litScore, wokeScore):
        self.name = name
        #woke or not-woke, only ever changed by fuctions
        self.role = ""
        #litpoints
        self.litScore = litScore
        #wokepoints
        self.wokeScore = wokeScore
        self.strijdInv = []

def scoreChange(player, typ, amount):
    """function to add and subtract points"""
    if typ == "lit":
        #takes either the player's new score or 0, whichever is higher
        player.litScore = max(0, player.litScore + amount)
    elif typ == "woke":
        #takes either the player's new score or 75, whichever is lower
        player.wokeScore = min(75, player.wokeScore + amount)
    #this else is purely for debugging purposes
    else:
        print("that's not an option >:(")

def input(message=''):
    """this method replaces the vanilla input() method with a custom one based on java: the given parameter is shown above the input of the textbox"""
    #this function relies on java libraries
    from javax.swing import JOptionPane
    #much like a regular input() method, this function returns the input as a string
    return JOptionPane.showInputDialog(frame, message)

def assignRoles():
    """adds the roles to the list: half of the players (rounded up) are woke, the others are lit"""
    global playerList
    roleList = []
    for i in range(len(playerList)//2):
        roleList.append("lit")
    for i in range(len(playerList)//2, len(playerList)):
        roleList.append("woke")
    #debug
    print(roleList)
    #calls the shuffle-method from the random library to shuffle the order of the role list
    shuffle(roleList)
    #debug
    print(roleList)
    #every player receives one of the randomly ordered roles
    for i in range(len(playerList)):
        playerList[i].role = roleList[i]
        
def checkAmount(string):
    global playerList
    players = int(input(string))
    if players >= 2 and players <= 8:
        for i in range (players):
            #give every player an id, name, role, and set the score to 0
            playerList.append(Player(input("Player %i, type your name: "%(i+1)), 0, 100))
    else:
        checkAmount("The amount of players has to be at least 2 and at most 8.")
    
def turnIncrement():
    global turnCount, currentPlayer, playerList
    print(currentPlayer.name)
    turnCount += 1
    #if turncount is higher than the amount of players, instead of letting it loop back to 0 (which takes valuable processing power!), we just take the modulo of the turncount and the amount of players for basically the same effect
    currentPlayer = playerList[turnCount%len(playerList)]
    

def setup():
    global playerList, turnCount, currentPlayer
    #put all the players in a list
    #internally, the players are identified by their position in the list: player 1 is playerList[0], for example
    playerList = []
    #this function defines the player objects and adds them to the playerlist
    checkAmount("How many players are there?")
    assignRoles()
    turnCount = 0
    currentPlayer = playerList[turnCount]
    
