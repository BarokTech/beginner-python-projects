'''
programmersAdventure Game!

This game is a text based game in which the player
in this case the programmer is offered conditions
to decide on.
Based on his decision he will move forward or lose the game.

'''
import sys

properTime = 6 #The assumed timeframe for quality production of the software

print("welcome to programmersAdventure world!")
print("You are making deal with a client on timeframe of the project you gonna work on. \n Stage 1")
answer = input('With the specified quality of product, how much time does it take you to finish?(in months)')
if int(answer) < 4:
    print("We need a properly tested project. \n You lose!")
    sys.exit()
elif int(answer) <= 7:
    print("Deal! Good coding!")
    print("Stage 2")
    print(f"You are at {int(answer) / 2}th Month")
    print("We have changed our mind. We need aditional functionalities to be included.")
    answer = input("Would you do that? (sure/ With added payment- wap)")
    if answer == "sure":
        print("Your time and effort worths. \n You lose!")
        sys.exit()
    elif answer == "wap":
        print("Deal!")
        print("Stage 3")
        print("Time for project's completion.")
        answer = input("How much of the project you completed! (out of 100)")
        if int(answer) == 100:
            print("You are a great and loyal programmer!")
            print("Here are the $$$$ and thank you! \n see you with another project!")
            sys.exit()
        else:
            print("You lost your reputation and cliens! \n You lose!")
            sys.exit()
elif int(answer) > 7:
    print("We are in a competitive market! \n You lose!")
    sys.exit()