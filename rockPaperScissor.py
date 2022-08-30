'''
This is the well known rockPaperScissor game.
rock beats scissor
scissor beats paper
paper beats rock
While playing the game, the result will be displayed as
wins = ... , ties = ..., Losses = ...

'''

import random, sys

#declaring global variables in order to be accessed by other functions in their scope
global wins
wins = 0
global losses 
losses= 0
global ties
ties = 0
global randomNumber
global computerMove
global playerMove

#A function for evaluating the results based on the logic above
def moveEvaluate(playerMove, computerMove):
    if playerMove == computerMove:
        global ties
        global wins
        global losses
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1 
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1


#A function for checking the player move and displaying simple string
def moveCheck(playerMove, randomNumber):
    global computerMove
    if playerMove == 'r':
        print('ROCk versus ', end='')
    elif playerMove == 'p':
        print('PAPER versus ', end='')
    elif playerMove == 's':
        print('SCISSORS versus ', end='')
    
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')


while True:
    #A score board to show results while playing
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    #A loop to check player input
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove =='r' or playerMove == 'p' or playerMove == 's':
            break
        else:
            print('Type one of r, p, s, or q.') #if the player inputs other character
    randomNumber = random.randint(1,3)

    #calling the functions a moveCheck() and moveEvaluate()
    moveCheck(playerMove, randomNumber)

    moveEvaluate(playerMove, computerMove)

