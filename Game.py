

import random
    
def playRound(roundNumber): #playRound function
    numberOfGuesses = 0     #guesses starts at 0
    randomNumber = random.randint(0, 100)   #generates random number between 0 to 100
    
    while True:     # this loop will run forever so that a round always begins until the user enter q to quit the game
        userGuess = input("Enter your guess between 1 to 100: ")    #Asking for a user input for guess
            
        if userGuess == "q":        # Checks if user input is q, so that you can quit the game
            print("The number was: {} ".format(randomNumber))       # prints the random number
            print("You took {} guesses in round {}".format(numberOfGuesses, roundNumber))       #prints the number of guesses you took
            return False
        try:
            userGuess = int(userGuess)  #Converts the input to a integer value
        except:
            print("You did not enter a valid integer, try again")       #Prints an error message of not entering an integer
            continue
        
        numberOfGuesses += 1    #the number of guesses goes up 1 when user guesses a number
        
        if userGuess == randomNumber:           # checks if the integer value of userGuess is equal to the random number                     
            print("How did you userGuess my number! Wow!!!")
            print("It took {} guesses in round {}\n".format(numberOfGuesses, roundNumber))  #prints the amount of guesses it took the user
            print("Entering round {}".format(roundNumber + 1))      #prints the next round number
            return True
        elif userGuess < randomNumber:  #checks if the integer value of userGuess is less than the random number
            print("My number is higher than yours, please guess again!")
        elif userGuess > randomNumber:  #checks if the integer value of userGuess is greater than the random number
            print("My number is lower than yours, please guess again!")
        
        if numberOfGuesses == 10:       # if the number of guesses is 10, prints message
            print("\n Keep Trying. You will eventually get it")
        if numberOfGuesses == 30:       # if the number of guesses is 30, prints message
            print("\n Lifes hard ain't it? I will give you the number it was {}".format(randomNumber))
            print("Thank You for playing")
            exit(0)


if __name__ == '__main__':
    name = input("Lets Introduce ourselves. My name is Gerald, the number guessing guru and you are? \n ")
    # asks the user for their name
    start = input("Hello, {}, nice to meet you. I want you to try to guess my number. Enter y to start playing! \n".format(name))
    # user enters keyword, 'y', to start the game
    if start.lower()!= "y":    #checks if the user did not enter y
        print("See You Soon")    #prints a goodbye message
        exit(0)     #exits program
    print("Just a heads up, enter q at any point to quit!")
    roundNumber = 1     #round starts at 1
    while True:     #this loop will run forever, no matter what, in this case its to start the game
        roundResult = playRound(roundNumber)
        roundNumber += 1    #the round number increases by 1 each time when user is entering the next round
        if not roundResult: # Exits the game if the round doesn't start
            print("Thank You for playing!")
            exit(0)




