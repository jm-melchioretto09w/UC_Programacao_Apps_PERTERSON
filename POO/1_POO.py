class Mobile:

    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color
        self.battery: int = 100
        self.on: bool = False

    def __str__(self):
        return f"Um {self.brand} {self.model} {self.color}:\n\tBateria: {self.battery}%\n\tEstado: {"Ligado" if self.on else "Desligado"}"

    def turnOn(self):
        if self.on:
            print(f"O seu {self.model} já está ligado")
        elif self.battery <= 0:
            print(f"O seu {self.model} está sem bateria")
        else:
            print(f"O seu {self.model} foi ligado")
            self.on = True

    def turnOff(self):
        if not self.on:
            print(f"O seu {self.model} já está desligado")
        else:
            print(f"O seu {self.model} foi desligado")
            self.on = False

celular = Mobile("Xiaomi", "Redmi 13", "Preto")
print(celular)
celular.turnOn()
celular.turnOn()
print(celular)
celular.turnOff()
celular.turnOff()
print(celular.brand)

print("\n=== OUTRO CELULAR===\n")

celefony = Mobile("Samsung", "Galaxy s23", "Branco")
celefony.battery = 0
print(celefony)
celefony.turnOn()
celefony.turnOn()
print(celefony)
celefony.turnOff()
celefony.turnOff()
print(celefony.brand)