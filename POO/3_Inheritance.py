from random import random


class Animal:
    def __init__ (self, name: str, scientificName: str, sound: str, weight: float) -> None:
        self.name = name
        self.scientificName = scientificName
        self.sound = sound
        self.weight = weight #in Kg

    def emmitSound(self):
        print(f"The {self.name} made {self.sound}")

    def __str__(self) -> str:
        return f"{self.name} - {self.scientificName}: {self.weight}Kg"

class Dog(Animal):
    def __init__ (self, name: str, weight: float):
        super().__init__(name, "Canis lupus familiaris", "Woof", weight)

    def bark(self):
        super().emmitSound()

    def dig(self, objects) -> str:
        print(f"{self.name} is digging something...")
        return random.choice(objects)


cat = Animal("Chapisco", "sla", "Meow", 12)
dog = Dog("Brutus", 20)

cat.emmitSound()
dog.bark()

print(cat, "\n",  dog)