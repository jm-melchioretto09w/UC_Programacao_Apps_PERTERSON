from typing import override


class Product:
    def __init__(self, name: str, price: float, storage: int = 0):
        self.name = name
        self.__price = price
        self.__storage = storage

    @property
    def price(self):
        return self.__price

    @property
    def storage(self):
        return self.__storage

    def insert(self, quantity: int):
        if quantity < 0:
            print("Quantidade inválida!!")
            return

        self.__storage += quantity
        print(f"Entrada: {quantity}. Novo estoque: {self.__storage}")

    def sell(self, storage):
        if storage < 0:
            print("Quantidade inválida!!")
            return

        if storage > self.__storage:
            print(f"Estoque insuficiente, temos apenas {self.__storage} {self.name}s")
            return

        else:
            self.__storage -= storage
            print(f"Vendidos: {storage}. Novo estoque: {self.__storage}")

    def __str__(self) -> str:
        return f"{self.name}:\n\tPreço: R${self.price:.2f}\n\tEstoque: {self.quantity} unidades\n\tValor total Estoque: {self.price * self.quantity}"

    @property
    def finalPrice(self):
        return self.price * 1.1

class Eletronic(Product):
    def __init__(self, name: str, price: float, warantyTime: int, storage: int = 0):
        super().__init__(name, price, storage)
        self.__warantyTime = warantyTime

    @override
    @property
    def finalPrice(self):
        return self.price * 1.2 + 5 * self.__warantyTime

class Food(Product):
    def __init__(self, name: str, price: float, expires: int, storage: int = 0):
        super().__init__(name, price, storage)
        self.__expires = expires

    @override
    @property
    def finalPrice(self):
        return self.price * 1.05

# Encapsulation - Tests
print("ENCAPSULATION")
prod = Product("Teste", 10.99, 20)
prod.insert(10)
prod.insert(-7)
prod.sell(40)
try:
    prod.storage = 9
except:
    print("Estoque inalterado")

# Inheritance - Tests
print("INHERITANCE")
elec = Eletronic("Tablet", 150, 12)
print(f"Eletronico é Produto? {isinstance(elec, Product)}")
food = Food("Meat", 90, 2)
print(f"Comida é Produto? {isinstance(food, Product)}")

# Polymorphism - Tests
print("POLYMORPHISM")
prods = [prod, elec, food]
print("Preços finais:")
for product in prods:
    print(f" ->\t{product.name} - R${product.finalPrice}")