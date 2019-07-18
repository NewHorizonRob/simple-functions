# This is a guess the number game 

import random #random module imported
secretNumber = random.randint(1,20) #randint function stored into the variable secretNumber
print("I'm thinking of a number between 1 and 20")

#Ask the player to guess 6 times
for guessesTaken in range(1,7): #gives the user 6 chances to guess the right number 
                                #this loop will only happen 6 times if the guess isn't right 
    print('Take a guess')
    guess = int(input()) # puts the user integer input into the variable guess

    if guess < secretNumber: #if the user's input is lower than secret number then run clause
        print ("Your guess is too low")
    elif guess > secretNumber: #else if the user's input is higher than the secret number then run clase
        print("Your number is too high")
    else: 
        break #this condition means that the user's guess is correct or incorrect 

if guess == secretNumber: #if the user's input is correct
    print("Congratulations you guessed my number in " + str(guessesTaken) + " guesses")
else: #else print this statement if the guesses were wrong 
    print("Nope. The number I was thinking of was " + str(secretNumber))