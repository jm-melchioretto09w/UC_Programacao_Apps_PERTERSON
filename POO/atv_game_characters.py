class Character():

    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.level = 1
        self.hp = 100

    def __str__(self) -> str:
        return f"{self.name}, {self.role}:\n\tLevel {self.level}\n\tHP: {self.hp}/100"

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} morreu!")

    def heal(self, points):
        self.hp += points

    def levelUp(self):
        self.level += 1
        self.hp = 100

char1 = Character("Bataterson", "Bárbaro")
print(char1)
char1.takeDamage(10)
print(char1)
char1.levelUp()
print(char1)
char1.takeDamage(100)
print(char1)