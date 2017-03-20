import csv
import Results
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
while not team in teams:
    team = easygui.choicebox("Pick your team", "Pick Team", teams)

posQuestAmount = ("01", "05", "10")
demQuestions = easygui.choicebox("How many questions?", "Questions", posQuestAmount)
while not demQuestions in posQuestAmount:
    demQuestions = easygui.choicebox("How many questions?", "Questions", posQuestAmount)

totRes = 0
random.shuffle(tqs)
for x in range(int(demQuestions)):
    totRes += ask_question(tqs[x])
print("Your " + team + " team score: " + str(totRes))

with open('scores.txt', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                        quotechar='^', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([totRes, team])