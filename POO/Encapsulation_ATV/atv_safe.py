class Safe:
    def __init__(self, password: str, maxTries: int):
        self.__password = password
        self.__itens = []
        self.__open = False
        self.__tries = 0
        self.__maxTries = maxTries
        self.__locked = False

    def open(self, password):
        if self.__open :
            print("O cofre já está aberto")
            return

        if self.__locked:
            print("/!\\ TRANCA DE SEGURANÇA ATIVA /!\\")
            return

        if password == self.__password:
            print("Senha correta inserida, cofre aberto")
            self.__open = True
            self.__tries = 0
        else:
            self.__tries += 1
            print(f"Senha incorreta! Tentativa {self.__tries} de {self.__maxTries}")

        if self.__tries >= self.__maxTries:
            print("/!\\ Cofre trancado como medida de segurança /!\\")
            self.__locked = True

    def close(self):
        if not self.__open:
            print("O cofre já está fechado")
            return

        print("Cofre fechado")
        self.__open = False

    def store(self, item):
        if not self.__open:
            print("Abra o cofre primeiro")
            return

        print(f"{item} foi guardadop no cofre")
        self.__itens.append(item)

    def seeItens(self):
        if not self.__open:
            print("Abra o cofre primeiro")
            return

        print("ITENS:")
        for item in self.__itens:
            print(f" ->\t{item}")


cofre = Safe("1234", 3)
cofre.store("Relógio")  # Abra o cofre primeiro!
cofre.open("0000")  # Senha incorreta! Tentativa 1 de 3.
cofre.open("1234")  # Cofre aberto.
cofre.store("Relógio")  # Relógio guardado.
cofre.seeItens()  # Itens: ['Relógio']
cofre.close()  # Cofre fechado.

cofre.open("1")  # Senha incorreta! Tentativa 1 de 3.
cofre.open("2")  # Senha incorreta! Tentativa 2 de 3.
cofre.open("3")  # Senha incorreta! Tentativa 3 de 3.

cofre.open("1234")  # Cofre bloqueado!