class BankAccount:
    def __init__(self, holder: str, balance: float = 0):
        self.holder = holder
        self.balance = balance

    def withdraw(self, value: float):
        if value > self.balance:
            print(f"Saldo insuficiente na conta de {self.holder}")
            return 0
        print(f"R${value} sacado na conta de {self.holder}")
        self.balance -= value
        return value

    def deposit(self, value: float):
        print(f"R${value} depositado na conta de {self.holder}")
        self.balance += value

    def statement(self):
        print(f"{self.holder}: R${self.balance}")

print("=== START ===")
conta1 = BankAccount("A")
conta2 = BankAccount("B", 500)
conta1.statement()
conta2.statement()

print("=== DEPOSITS ===")
conta1.deposit(200)
conta2.deposit(200)
conta1.statement()
conta2.statement()

print("=== WITHDRAWS ===")
conta1.withdraw(300)
conta2.withdraw(300)
conta1.statement()
conta2.statement()