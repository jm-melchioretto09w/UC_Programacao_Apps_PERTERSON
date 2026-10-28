class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
        self.age = 0

    def bark(self):
        print(f"{self.name} barked: \"Woof woof!\"")

    def __str__(self) -> str:
        return f"{self.name} the {self.breed}: {self.age} years old"

dog1 = Dog("Rex", "Bulldog")
dog2 = Dog("Laika", "Pinscher")
print(dog1)
print(dog2)
dog2.age = 15
print(dog1)
print(dog2)