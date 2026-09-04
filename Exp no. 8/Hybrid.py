class Animal:
    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


class Hybrid(Dog, Cat):
    def display(self):
        print("Hybrid inheritance")


h = Hybrid()

h.eat()
h.bark()
h.meow()
h.display()
