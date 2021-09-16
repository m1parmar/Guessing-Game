
import random
    
def playRound(roundNumber):
    numberOfGuesses = 0     
    randomNumber = random.randint(0, 100)   #generates random number between 0 to 100
    
    while True:     
        userGuess = input("Enter your guess between 1 to 100: ")    #Asking for a user input for guess
            
        if userGuess == "q":      
            print("The number was: {} ".format(randomNumber))     
            print("You took {} guesses in round {}".format(numberOfGuesses, roundNumber))       
            return False
        try:
            userGuess = int(userGuess)  
        except:
            print("You did not enter a valid integer, try again")      
            continue
        
        numberOfGuesses += 1    #the number of guesses goes up 1 when user guesses a number
        
        if userGuess == randomNumber:                            
            print("How did you userGuess my number! Wow!!!")
            print("It took {} guesses in round {}\n".format(numberOfGuesses, roundNumber))  
            print("Entering round {}".format(roundNumber + 1))      
            return True
        elif userGuess < randomNumber:  
            print("My number is higher than yours, please guess again!")
        elif userGuess > randomNumber:  
            print("My number is lower than yours, please guess again!")
        
        if numberOfGuesses == 10:      
            print("\n Keep Trying. You will eventually get it")
        if numberOfGuesses == 30:      
            print("\n Lifes hard ain't it? I will give you the number it was {}".format(randomNumber))
            print("Thank You for playing")
            exit(0)


if __name__ == '__main__':
    name = input("Lets Introduce ourselves. My name is Gerald, the number guessing guru and you are? \n ")
   
    start = input("Hello, {}, nice to meet you. I want you to try to guess my number. Enter y to start playing! \n".format(name))
   
    if start.lower()!= "y":    
        print("See You Soon")    
        exit(0)     #exits program
    print("Just a heads up, enter q at any point to quit!")
    roundNumber = 1    
    while True:   
        roundResult = playRound(roundNumber)
        roundNumber += 1    
        if not roundResult: 
            print("Thank You for playing!")
            exit(0)


