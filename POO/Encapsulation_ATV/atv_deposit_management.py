class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    def insert(self, quantity: int):
        if quantity < 0:
            print("Quantidade inválida!!")
            return

        self.__quantity += quantity
        print(f"Entrada: {quantity}. Novo estoque: {self.__quantity}")

    def take(self, quantity):
        if quantity < 0:
            print("Quantidade inválida!!")
            return

        if quantity > self.__quantity:
            print(f"Estoque insuficiente, temos apenas {self.__quantity} {self.name}s")
            return

        else:
            self.__quantity -= quantity
            print(f"Saída: {quantity}. Novo estoque: {self.__quantity}")

    def applyDiscount(self, discount: int):
        if discount < 1 or discount > 50:
            print("O desconto deve ser de 1% á 50%")
            return

        self.__price *= (100 - discount)/100
        print(f"Desconto: {discount}%. Novo preço: {self.__price}")

    @property
    def storageValue(self):
        return self.__price * self.__quantity

fone = Product("Fone Bluetooth", 150.0, 10)
fone.take(3)# Saída de 3. Estoque: 7
fone.take(20)# Estoque insuficiente! Disponível: 7
fone.insert(-5)# Quantidade inválida!
fone.applyDiscount(80)# Desconto deve ser entre 1% e 50%!
fone.applyDiscount(10)# Novo preço: R$ 135.00
print(f"R$ {fone.storageValue:.2f}")   # R$ 945.00