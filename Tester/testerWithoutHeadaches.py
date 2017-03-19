import csv

import easygui
import test_question
import random

# This opens up the file with our questions
with open('Questions.txt') as file:
    reader = csv.reader(file, delimiter="\t")
    lines = list(reader)
    tqs = []
    for line in lines:
        tqs.append(test_question.TestQuestion(line))


with open('Teams.txt') as file:
    reader = csv.reader(file, delimiter="\t")
    lines = list(reader)
    teams = []
    for line in lines:
        if len(line):
            teams.append(line[0])


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


team = easygui.choicebox("Pick your team", "Pick Team", teams)

totRes = 0
random.shuffle(tqs)
for x in range(4):
    totRes += ask_question(tqs[x])
print("Your (" + team + ") score: " + str(totRes))
