
"""
Problem:  Implement the inheritance function where the overriding happens
          So neglate the constructor overriding using the super() keyword.

Sample Input : User define  

Platform: Self study

Difficulty: Easy 

"""


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        # Store breed


dog = Dog("Tommy", "Labrador")

print(dog.name)
print(dog.breed)