

# Each line from file contains six tab separated entries:
# question, correct answer, and three other possible wrong answers
class TestQuestion:
    def __init__(self, values):
        self.question = values[0]
        self.answer = values[1]
        self.possibles = values[1:5]
