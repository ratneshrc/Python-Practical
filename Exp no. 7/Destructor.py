class Student:
    def __del__(self):
        print("Destructor called")

s = Student()
del s
