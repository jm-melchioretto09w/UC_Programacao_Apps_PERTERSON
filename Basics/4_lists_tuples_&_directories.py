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

print(len(names))

for name in names:
    print(name)

if "Barbie" and "Andrew" and "KelP" in names:
    print("BFFs found")
else:
    print("Someone's missing")

data = ["batata", 12, True]
print(data)

marks = [10, 8, 9]
sumMarks: int = 0
for mark in marks:
    sumMarks += mark

avg = sumMarks/len(marks)
print(avg)

#tuples
coords = (3, 5)
#same as list but fixed (static)

#dictionaries
ctw = {
    "JM": "MI82",
    "KelP": "ME81",
    "T2": "MI82",
    "Kings": ""
}

print(ctw["Kings"])