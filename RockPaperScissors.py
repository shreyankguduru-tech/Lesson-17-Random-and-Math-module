import random

while True:
    userAction = input("Enter your action (Rock), (paper), (scissors)")
    PossibleAction = ["rock", "scissors", "paper"]
    computerAction = random.choice(PossibleAction)

    print("\nYou chose the action {userAction},The computer chose the action{computerAction}.\n")
    if userAction == computerAction:
        print("both players have chosen", userAction, "its a tie")
    elif userAction == "rock":
        if computerAction == "paper":
            print("You chose", userAction,"the computer chose", computerAction)
            print("you lose")
        else: 
            print ("You chose", userAction,"the computer chose", computerAction)
            print("you win")
    elif userAction == "paper":
        if computerAction == "scissors":
            print("You chose", userAction,"the computer chose", computerAction)
            print("you lose")
        else:
            print ("You chose", userAction,"the computer chose", computerAction)
            print("you win")
    elif userAction == "scissors":
        if computerAction == "rock":
            print("You chose", userAction,"the computer chose", computerAction)
            print("you lose")
        else:
            print ("You chose", userAction,"the computer chose", computerAction)
            print("you win")
    playAgain = input("would you like to play again? (y/n)")
    if input != "y":
        break


