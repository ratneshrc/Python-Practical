class A:
    def __init__(self):
        self.__x = 10      # Private
        self._y = 20       # Protected

    def __private(self):
        print("Private function")

    def _protected(self):
        print("Protected function")

    def show(self):
        print(self.__x)
        self.__private()


class B(A):
    def display(self):
        print(self._y)
        self._protected()


class C(B):
    pass


obj = C()
obj.show()
obj.display()
