names = ["A", "JM", "T2", "LL", "Mr. Miku", "KelP", "Andrew"]
print(names)# -> printa a lista inteira

print(names[0])# -> pega o item específico
print(names[-1])# se for negativo começa de trás pra frente (-1 -> último elemento)

names[4] = "Bot"
print(names)

names.append("Barbie")
print(names)

names.insert(0, "Nena")
print(names)

names.remove("A")
print(names)

names.pop(1)
print(names)