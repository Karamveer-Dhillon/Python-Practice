import random
Turn=("Rock","Paper","Scissors")#Computer's turn
Computer=Turn[random.randint(0,2)]

Player=False

while Player==False:

    Player = input("Rock, Paper, Scissors?")#Player's turn
    
    if Player.upper()==Computer.upper():#Tie
        print("Tie!")
    
    elif Player.upper()=="ROCK":#Player has Rock
        if Computer=="SCISSORS":
            print(Computer+" You Win!: Rock Smashes Scissors")
        else:
            print(Computer+" You Lose!:Paper Covers Rock")
    
    elif Player.upper()=="PAPER":#Player has Paper
        if Computer=="ROCK":
            print(Computer+" You Win!: Paper Covers Rock")
        else:
            print(Computer+" You Lose!:Scissors Cuts Paper")
    
    elif Player.upper()=="SCISSORS":#Player has Scissors
        if Computer=="Paper":
            print(Computer+" You Win!: Scissors Cuts Paper")
        else:
            print(Computer+" You Lose!:Rock Smashes Scissors")
            
    else:
        print("Wrong Input: Please Chose from Rock, Paper, Scissors")#Wrong input
        
    Player=False
    Computer=t[random.randint(0,2)]