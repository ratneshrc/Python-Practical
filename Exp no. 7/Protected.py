class Student:
    def __init__(self):
        self._name = "Meowth"

class Result(Student):
    def display(self):
        print(self._name)

r = Result()
r.display()
