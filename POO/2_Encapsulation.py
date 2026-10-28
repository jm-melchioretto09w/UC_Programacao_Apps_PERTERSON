#Usaremos a classe BankAccount para demonstrar o encapsulamento

#Privacidade do atributo:
# nome -> público
# _nome -> protegido
# __nome -> privado

class BankAccount:
    def __init__(self, holder: str, balance: float = 0):
        self.holder = holder
        self.__balance = balance

    def withdraw(self, value: float):
        if value > self.__balance:
            print(f"Saldo insuficiente na conta de {self.holder}")
            return 0
        print(f"R${value} sacado na conta de {self.holder}")
        self.__balance -= value
        return value

    def deposit(self, value: float):
        print(f"R${value} depositado na conta de {self.holder}")
        self.__balance += value

    @property
    def statement(self):
        return f"{self.holder}: R${self.__balance}"

    @property
    def getBalance(self):
        return self.__balance

conta = BankAccount("Ana", 1000)
print(conta.statement)

try:
    conta.holder = "Batata"
    print("Holder alterado para \"Batata\"")
except AttributeError:
    print("Erro ao alterar Holder, valor é privado!")

try:
    conta.getBalance = 7
    print("Balance alterado para 7")
except AttributeError:
    print("Erro ao alterar Balance, valor é privado!")

print(conta.statement)