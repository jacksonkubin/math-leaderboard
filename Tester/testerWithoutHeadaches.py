import csv

import easygui
import TestQuestion
import random

#This opens up the file with our questions
with open('Questions.txt') as file:
    reader = csv.reader(file, delimiter="\t")
    lines = list(reader)
    tqs = []
    for line in lines:
        tqs.append(TestQuestion.TestQuestion(line))

def AskQuestion(tq):
    a = tq.possibles
    random.shuffle(a)
    q = easygui.buttonbox(tq.question, "?", choices=(a[0], a[1], a[2], a[3]))
    answer = tq.answer
    if (q == answer):
        result = 1
        easygui.msgbox("Yay!")
    else:
        result = 0
        easygui.msgbox("Try again!")
    return result

random.shuffle(tqs)
for x in range(0, 4):
    print(AskQuestion(tqs[x]))