import csv

from Tkinter import *
import Tkinter as tk

import random

import TestQuestion
import QuestionUI


#This opens up the file with our questions
with open('Questions.txt') as file:
    reader = csv.reader(file, delimiter="\t")
    lines = list(reader)
    tqs = []
    for line in lines:
        tqs.append(TestQuestion.TestQuestion(line))

# Our framework for tk is set up here.
root = tk.Tk()
# root.geometry('800x600')
# root.attributes('-fullscreen', True)
root.configure(background='navy')

#Keys are getting registered that they are getting pressed here
##def key(event):
##    print("pressed", repr(event.char))

#root.bind("<Key>", key)



# This sets up the UI

# Ask randomized questions
random.shuffle(tqs)
for x in range(0, 4):
    qui = QuestionUI.QuestionUI(root)
    print(qui.AskQuestion(tqs[x]))

# root.pack(fill='both')

# This centers the grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(6, weight=1)

# root.mainloop()
