name = input("Qual o nome do personagem?\n")
role = input("Qual a classe do personagem?\n")
age = int(input("Qual a idade do personagem?\n"))
level = int(input("Qual o nível do personagem?\n"))
xp = float(input("Quantos xp o personagem tem?\n"))
hp = float(input("Quantos hp o personagem tem?\n"))
hpTotal = hp

print(f"{name} - {role} - {age} anos\n\tXP: {xp}\n\tHP: {hp}/{hpTotal}")

print(type(name))
print(type(age))
print(type(xp))

hp -= 10

print(hp)

xp += 1000

print(xp)

age *= 2

print(age)

hp /= 4

print(hp)

print(hp % 2)