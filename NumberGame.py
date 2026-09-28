import random
playing = True
number = str(random.randint(0,9))


print("I will generate a number from 0 to 9 and you have to guess the number one digit at a time")
print("the game ends once you guess it correctly")

while playing:
    guess = input("Give me your best guess:\n")
    if guess == number:
        print ("Correct")
        break
    else:
        print("wrong try again")
        