class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    def apresentar(self):
        print(f"Nome: {self.name}")
        print(f"Salario: R$ {self.__salary:.2f}")

    def giveRaise(self, percentage):
        if percentage <= 0:
            print(f"Aumento inválido!")
            return
        else:
            self.__salary = self.__salary * (1 + (percentage / 100))
            print(f"{self.name} recebeu {percentage}% de aumento.")

    def bonus(self):
        return self.salary * 0.1


class Manager(Employee):
    def __init__(self, name, salary, teamSize):
        super().__init__(name, salary)
        self.teamSize = teamSize

    def bonus(self):
        return self.salary * 0.2 + self.teamSize * 100


class Trainee(Employee):
    def __init__(self, name, salary, course):
        super().__init__(name, salary)
        self.curso = course

    def bonus(self):
        return 200

team = [
    Employee("Ana", 3000),
    Manager("Bruno", 8000, 5),
    Trainee("Caio", 1500, "Análise de Sistemas")
]

print("BONUS:")
for employee in team:
    print(f" ->\t{employee.name}: R${employee.bonus()}")