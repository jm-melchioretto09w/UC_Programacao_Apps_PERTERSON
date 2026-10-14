#while
print("while")
i = 1
while i <= 5:
    print(i)
    i += 1

#for
print("\nfor")
for n in range(1,6):
    print(n)

#for each
names = ["A", "JM", "T2", "LL", "Mr. Miku", "KelP", "Andrew"]

for name in names:
    print(name)

#break (mata o loop)
for m in range(1, 11):
    if m == 6:
        break
    print(m)

#continue (pula para o próximo)
for m in range(1, 11):
    if m == 6:
        continue
    print(m)

#pass (segue o baile)
for m in range(1, 11):
    if m == 6:
        pass
    print(m)

