#Francis Adepoju, 2018-02-14
#Guessing Game 
#Adapted from: https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-9

from random import randint

target = randint(1, 100)
guess  = 0
#print("Target is: ", target)
print ("Guess a number between 1 and 100:  ")
while guess != target:
    guess = int(input("Please enter your guess:   "))
    if guess == target:
        print("Well done! You guessed correctly")
    elif guess < target:
        print("Too low, increase your number please.")
    else:
        print("Too high, please reduce!")
