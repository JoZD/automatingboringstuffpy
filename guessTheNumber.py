


#Guess the number 

import random






def createRandomNumber():
    number = random.randint(1,20)
    return number



    #ask the user and give 6 attempts 



def game():
    number = createRandomNumber()
    
    name = input("Please enter your name:\n")
    print(f"Hello {name.title()} I'm thinking about a number, can you guess? \n")
 

    for i in range(1, 7):
        print("Take a guess :) \n")
        guess = int(input("Please enter your guess:\n"))
            
        if  guess < number: 
            print(f"Oops! The number is greater than {guess}")
        elif guess > number:
            print(f"Oops! The number is lower than {guess}")
        else: 
            break
            
    if guess == number:
        print(f"Congratulations {name.title()} {guess} was the number\n")
        flag = input(f"Want to play again? (y/n)")
        if flag == 'y':
            createRandomNumber()
            game()



createRandomNumber()
game()


# ---------------------------------------------------------------- Code tested  and it works!   




            