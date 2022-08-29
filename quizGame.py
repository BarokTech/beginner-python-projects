'''

This is a simple quize project.
The player is asked to input answers for 5 questions.
Answering 3 or more questions is a win and failing to do that is a lose.

'''
score = 0
print('This is quizGame!') 
print('You are going to be asked 5 questions about Python.')
#The answer key list
AnswerKey = ["Guido", "dynamic", "import", "fs", "print"]
i = 0
while(i < 5):
    
    if i == 0:
        #To request the user the answer for the question and storing that in the 'answer' varible
        answer = input("Who is the person who created pythn? \n ")
        #Checking the answers the user inserts with the ones stored in the answer key after converting both to lower cases
        if answer.lower() == AnswerKey[0].lower():
            #incrementing the score of the player after answering correctly
            score += 1
    elif i == 1:
        answer = input("What programming paradigm does  Python follow? (static / dynamic)")
        if answer.lower() == AnswerKey[1].lower():
            score += 1
    elif i == 2:
        answer = input("What is the key word to use external modules in python?")
        if answer.lower() == AnswerKey[2].lower():
            score += 1
    elif i == 3:
        answer = input("What is the name of the Python module to work with file system?")
        if answer.lower() == AnswerKey[3].lower():
            score += 1
    elif i == 4:
        answer = input("What key word do we use to display a text to the screen in python?")
        if answer.lower() == AnswerKey[4].lower():
            score += 1
    i += 1 #To increment the looping variable by 1
    


if score >= 3:
    print(f"You scored {score} out of 5. \n You Won!")
else:
    print(f"You scored {score} out of 5. \n You lose!")

