#! python 3.10.4, Dhruv Ramaswamy, dhruvcopy1.0
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import random
import os
from pathlib import Path

# The quiz data. Keys are states and values are their capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Generate 35 quiz files.

# Create two new folders
def getFolderForTest():
    validName = False
    global counterBecausePythonDoesntHaveForLoops
    counterBecausePythonDoesntHaveForLoops = 1
    while not validName:
        path = Path(Path.cwd(), f'_Test_Sheets{counterBecausePythonDoesntHaveForLoops}')
        if not Path.exists(path):
            os.makedirs(path)
            validName = True
        else:
            counterBecausePythonDoesntHaveForLoops += 1
    return path


def getFolderForAnswers():
    validName = False
    _counter = 0
    while not validName:
        name = '_Answer_Sheets' + ('_' * _counter) + str(counterBecausePythonDoesntHaveForLoops)

        if not Path.exists(Path(Path.cwd(), Path(name))):
            os.makedirs(Path(Path.cwd(), Path(name)))
            newPath = Path(Path(Path.cwd(), Path(name)))
            validName = True
        else:
            _counter += 1
    return newPath


folderWhichHaveTheQuizzes = getFolderForTest()
folderWhichHaveTheAnswers = getFolderForAnswers()

for quizNum in range(35):

    # Create quiz/answer key files

    # Changes the current working directory
    os.chdir(folderWhichHaveTheQuizzes)
    quizfile = open(f'capitals-quiz{quizNum + 1}.txt', 'w')  # Create files with the open() function
    os.chdir(folderWhichHaveTheAnswers)
    answerKeyFile = open(f'capitals-quiz_answers{quizNum + 1}.txt', 'w')  # Create the answer key file

    os.chdir(folderWhichHaveTheQuizzes)
    # Writing boilerplate for the quiz
    quizfile.write('Name:\n\nDate:\n\nClass:\n\n')
    quizfile.write((' ' * 20) + f'State Capital Quiz (Form {quizNum + 1})')
    quizfile.write('\n\n')

    # Shuffling the list of capital's states
    states = list(capitals.keys())  # Takes the keys and puts them into alist
    random.shuffle(states)  # Shuffles the keys

    # This will loop through states in the shuffled 'states' list, get wrong and right answers, and write it to the file
    for questionNum in range(50):

        # 'state' is the current state that we be quizzing about
        correctAnswer = capitals[states[questionNum]]  # Gets correct answer for each state

        # To get the wrong answers, you duplicate all the values
        wrongAnswers = list(capitals.values())

        # Delete the correct answer, by taking correctAnswer/finding what index it is in 'wrongAnswers' is & deletes it
        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        # Sample three random values to ensure no duplicates
        wrongAnswers = random.sample(wrongAnswers, 3)

        # Combines the right answer and the wrong answers, and then shuffles them
        answerOptions = [wrongAnswers[0]] + [correctAnswer] + [wrongAnswers[1]] + [wrongAnswers[2]]
        random.shuffle(answerOptions)

        # Now, we write everything to the quiz-file!!

        # Questions section

        # Changes the path to the folder which has the quizzes
        os.chdir(folderWhichHaveTheQuizzes)
        quizfile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

        # Writing answer options to the quiz file and formatting them
        for i in range(4):
            quizfile.write(f"      {'ABCD'[i]}. {answerOptions[i]}\n")
        quizfile.write('\n')

        # Writing answers

        # Changes to the folder with the answers
        os.chdir(folderWhichHaveTheAnswers)
        # Writes the question number, and writes out the correct answer in letter form
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]} \n")

# Close the quiz file/answer files/folders
quizfile.close()
answerKeyFile.close()

print(f"Created! dhruvcopy1.0. More features to come soon on github (dhruvramaswamy)\nDirectory of quizzes: {folderWhichHaveTheQuizzes}\nDirectory of answers: {folderWhichHaveTheAnswers}")
