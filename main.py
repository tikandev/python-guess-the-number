#Importing Python module random for random number generation
import random

#Setting default values for the two variables used later
guess = None
guessCount = 0

#Function for checking if earlier hiscore exists. Hiscore isn't included in the repository for the sake of testing.
def get_hiscore():
    hiscore = 0

    #Checking if the hiscore file exists. Score will be read from the file if it exists.
    try:
        hiscore_file = open("hiscore.txt","r")
        hiscore = int(hiscore_file.read())
        hiscore_file.close()
        print("The current lowest amount of guesses is:", hiscore)
    except IOError:
        print("There is no existing hiscore yet for this game.")
    
    return hiscore

#Function to save the new hiscore/lowest amount of guesses set by the player
def save_hiscore(new_hiscore):
    try:
        hiscore_file = open("hiscore.txt","w")
        hiscore_file.write(str(new_hiscore))
        hiscore_file.close()
    except IOError:
        #Printing error line if for some reason the score can't be saved.
        print("Was unable to save the hiscore.")

print("Hi! In this game I will choose a number between 1 and 100. You will then try to guess the number.")
print("Let's begin!")

hiscore = get_hiscore()

#Generating a random number between 1 and 100 for the guessing game
number = random.randint(1,100)

#Asking the player to guess a number until the guess is right. With every wrong guess the player is advised to either try a lower or higher number and the guesses are being counted.
#However if the player is guessing a number out of the given range (1-100) or the input is otherwise invalid the guess is not being counted.
while guess != number:
    guess = int(input("Enter your guess: "))

    if guess == number:
        guessCountString = str(guessCount)
        print("Congratulations! You guessed right!")
        print("It took you " + guessCountString + " guesses to get the number right!")
        if guessCount < hiscore or hiscore == 0:
            print("Congratulations! You also made a new hiscore!")
            save_hiscore(guessCount)
        else:
            print("You didn't manage to set a new hiscore, too bad.")
    elif guess > number and guess <= 100:
        print("That's not it, try again with a lower number.")
        guessCount += 1
    elif guess < number and guess >= 1:
        print("That's not it, try again with a higher number.")
        guessCount += 1
    else:
        print("Please guess a number between 1 and 100.")