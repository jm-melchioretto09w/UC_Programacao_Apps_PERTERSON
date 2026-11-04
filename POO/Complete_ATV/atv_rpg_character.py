from __future__ import annotations

from typing import override


class Character:
    def __init__(self, name: str):
        self.name = name
        self.__hp = 100

    @property
    def hp(self):
        return self.__hp

    def takeDamage(self, damage: int):
        if damage < 0:
            print("Dano inválido")
            return

        self.__hp -= damage

        if self.__hp < 0:
            self.__hp = 0

    def heal(self, heal: int):
        if heal < 0:
            print("Cura inválido")
            return

        self.__hp += heal

        if self.__hp > 100:
            self.__hp = 100

    def __str__(self) -> str:
        return f"{self.name} - {self.hp}/100 hp"

    @property
    def damage(self):
        return 10

    def attack(self, other: Character):
        other.takeDamage(self.damage)

class Warrior(Character):
    def __init__(self, name: str, power: int):
        super().__init__(name)
        self.__power = power

    @override
    @property
    def damage(self):
        return 10 + self.__power

class Mage(Character):
    def __init__(self, name: str, mp: int):
        super().__init__(name)
        self.__mp = mp
        self.__maxMP = mp

    @override
    @property
    def damage(self):
        if self.__mp < 10:
            return 5
        else:
            return 25

    @override
    def attack(self, other: Character):
        other.takeDamage(self.damage)
        if self.damage == 25:
            self.__mp -= 10

    def recharge(self):
        self.__mp = self.__maxMP

# Encapsulation - Tests
print("ENCAPSULATION")
char = Character("Batata")
char.takeDamage(10)
print(char)
char.takeDamage(-5)
print(char)
char.heal(20)
print(char)

try:
    char.hp = 101
except:
    print("Vida inalterada")

print(char)

# Inheritance - Tests
print("INHERITANCE")
warr = Warrior("A", 10)
mage = Mage("B", 50)

print(f"Guerreiro é personagem?\n{isinstance(warr, Character)}")
print(f"Mago é personagem?\n{isinstance(mage, Character)}")

# Polymorphism - Test
print("POLYMORPHISM")
chars = [Character("A"), Warrior("B", 10), Mage("C", 50)]
print("Ataques:")
for char in chars:
    print(f" ->\t{char.name} - {char.damage}hp")

#Batalha
print("BATTLE")
guerreiro = Warrior("T2", 10)
mago = Mage("TVzinha", 50)
turno = 1
while guerreiro.hp > 0 and mago.hp > 0:
    print(f"Turno {turno}:")
    guerreiro.attack(mago)
    print(f"{guerreiro.name} ataca {mago.name} com {guerreiro.damage} de dano")
    print(mago)
    mago.attack(guerreiro)
    print(f"{mago.name} ataca {guerreiro.name} com {mago.damage} de dano")
    print(guerreiro)

if guerreiro.hp <= 0:
    print(f"{guerreiro.name} foi derrotado")
if mago.hp <= 0:
    print(f"{mago.name} foi derrotado")