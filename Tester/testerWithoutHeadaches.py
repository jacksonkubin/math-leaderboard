import csv
import easygui
import test_question
import random


def show_leader_board():
    scores = get_scores()
    board = '\n'.join([str(x) for x in scores])
    easygui.textbox('Teams        Score', 'Leader Board', board)


def get_scores():
    with open('scores.txt') as scoresFile:
        reader = csv.reader(scoresFile, delimiter="\t", quotechar='^')
        lines = list(reader)
        scores = []
        for line in lines:
            scores.append(line[0] + '\t' + line[1])
    return scores


def show_play():
    with open('Teams.txt') as teamsFile:
        reader = csv.reader(teamsFile, delimiter="\t")
        lines = list(reader)
        teams = []
        for line in lines:
            if len(line):
                teams.append(line[0])

    team = easygui.choicebox("Pick your team", "Pick Team", teams)
    while not team in teams:
        team = easygui.choicebox("Pick your team", "Pick Team", teams)

    posQuestAmount = ("01", "05", "10")
    demQuestions = easygui.choicebox("How many questions?", "Questions", posQuestAmount)
    while not demQuestions in posQuestAmount:
        demQuestions = easygui.choicebox("How many questions?", "Questions", posQuestAmount)

    # This opens up the file with our questions
    with open('Questions.txt') as questionsFile:
        reader = csv.reader(questionsFile, delimiter="\t")
        lines = list(reader)
        tqs = []
        for line in lines:
            tqs.append(test_question.TestQuestion(line))

    totRes = 0
    random.shuffle(tqs)
    for x in range(int(demQuestions)):
        totRes += ask_question(tqs[x])
    print("Your " + team + " team score: " + str(totRes))

    with open('scores.txt') as scoresFile:
        reader = csv.reader(scoresFile, delimiter="\t",quotechar='^')
        lines = list(reader)

    with open('scores.txt', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='^', quoting=csv.QUOTE_MINIMAL)
        for line in lines:
            writer.writerow(line)
        writer.writerow([team, totRes])


def ask_question(tq):
    a = tq.possibles
    random.shuffle(a)
    q = easygui.buttonbox(tq.question, "?", choices=[a[0], a[1], a[2], a[3]])
    answer = tq.answer
    if q == answer:
        result = 1
        easygui.msgbox("Yay!")
    else:
        result = 0
        easygui.msgbox("Try again!")
    return result


ms = ['Leader board', 'Play', 'Quit']
mainMenu = ""
while not mainMenu in ms:
    mainMenu = easygui.choicebox('Welcome! We are very excited to have you here to play the Acolympics!',
                                 'Pick what to do', ms)
if mainMenu == 'Leader board':
    show_leader_board()
elif mainMenu == 'Play':
    show_play()
