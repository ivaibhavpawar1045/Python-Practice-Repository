"""
Problem:  Program that shows the concept of Object Oriented

Platform: SelfStudy

Difficulty: Mid

"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some sound"


class Dog(Animal):  # Dog inherits from Animal
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):  # Cat inherits from Animal
    def speak(self) -> str:
        return "Meow!"


dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says:", dog.speak())
print(cat.name, "says:", cat.speak())