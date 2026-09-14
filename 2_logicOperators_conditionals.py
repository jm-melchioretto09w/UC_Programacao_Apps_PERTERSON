num0 = int(input("Primeiro número: "))
num1 = int(input("Segundo número: "))

print(num0 == num1)
print(num0 != num1)
print(num0 < num1)
print(num0 > num1)
print(num0 <= num1)
print(num0 >= num1)

if num0 == num1:
    print("os números são iguais")
else:
    print("os números não são iguais")

#você pode combinar condições com "and", "or" e  "not" onde:
#and -> ambos tem de ser verdade para dar true
#or -> ao menos um deles tem de ser verdade para dar true
#not -> o valor tem q ser mentira para dar true