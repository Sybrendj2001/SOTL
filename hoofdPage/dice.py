def draw():
    global die_1, die_2, loadImage, img1, img2, img3, img4, img5, img6
    #the setup of the global values and functions. This comes FIRST
    die_1 = 0
    die_2 = 0
    img1 = loadImage(ScreenShot2019-12-09at10.15.15.jpg.png)
    img2 = pass
    img3 = pass
    img4 = pass
    img5 = pass
    img6 = loadImage(ScreenShot2019-12-0910.15.22.png)

    #this is a function to throw the dice. It will change the global values of die_1 and die_2. This comes SECOND
    def ThrowDice():
        global die_1, die_2
        die_1 = int(random(1,6))
        die_2 = int(random(1,6))
 #for what will we use Throwscore??????????????       
         Throwscore = die_1 + die_2
        return Throwscore
    
#this is a helper function that takes the values of throwdice as arguments to load the correct picture. This comes THIRD
    def ShowDice(die_1, die_2):
        global die_1, die_2, loadImage, img1, img2, img3, img4, img5, img6
        if die_1 == 1:
            die_1 = img1
        if die_1 == 2:
            die_1 = img2
        if die_1 == 3:
            die_1 = img3
        if die_1 == 4:
            die_1 = img4
        if die_1 == 5:
            die_1 = img5
        if die_1 == 6:
            die_1 = img6
        #die 2 is being checked and the picture will be loaded
        if die_2 == 1:
            die_2 = img1
        if die_2 == 2:
            die_2 = img2
        if die_2 == 3:
            die_2 = img3
        if die_2 == 4:
            die_2 = img4
        if die_2 == 5:
            die_2 = img5
        if die_2 == 6:
            die_2 = img6
        def ShowDiceWhere(die_1, die_2):
            imageMode(CENTER)
            image(die_1, 50, 50, 80, 80)
            imageMode(CORNER);
            image(die_2, 10, 10, 50, 50)
    
        
               
    
