class A:
    __private = 10
    _protected = 20

    def show(self):
        print(self.__private)
        print(self._protected)

class B(A):
    pass

class C(B):
    pass

C().show()
