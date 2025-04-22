# Who's a Good Dog?

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy", "Labrador")
dog.bark()
