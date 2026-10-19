class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}|R${self.price}/u|{self.quantity}u|SUBTOTAL|R${self.subtotal()}"

    def subtotal(self) -> float:
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.itens = []

    def add(self, product: Product):
        self.itens.append(product)

    def total(self) -> float:
        total = 0.0
        for iten in self.itens:
            total += iten.subtotal()
        return total

    def receipt(self):
        for iten in self.itens:
            print(iten)
        print(f"TOTAL: R${self.total()}")

prod1 = Product("A", 1, 2)
prod2 = Product("B", 2, 2)
prod3 = Product("C", 2, 4)
cart = Cart()
cart.add(prod1)
cart.add(prod2)
cart.add(prod3)
print(cart.total())
cart.receipt()