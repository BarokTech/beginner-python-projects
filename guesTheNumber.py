'''
This is a guesing game project.
The player is asked to input a number in range of 1 - 10.
The program checks the inputed number with the one it
 generates using the 'random' module.
If it matches the player wins.
If not the program gives up to 3 chances.

'''

#To import the 'random' module from Python library
import random

trial = 0
print("Welcome to guesTheNumber game!")
print("You have 3 chances")
#initializing a variable with generated random number in range of 1 - 10
num = random.randrange(1,5,1)

while(trial < 3):
    print(num)
    gues = input("Insert a number between 1 and 10: ")
    if int(gues) == int(num): #checking if the gues is equal with the generated value
        win = True # A boolean variable to hold winning status
        trial += 1
        break
    else:
        win = False
        trial += 1
        continue

#checking the winning status and outputing the result
if win == True:
    print(f"You won after {trial} tries!")
else:
    print(f"You lose after taking {trial} tries!")