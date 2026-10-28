class Studen:
    def __init__(self, name: str, mark: float):
        self.name = name
        if mark < 0 or mark > 10 :
            print("Improper grade, must be between 0 and 10, the value will be set to 0")
        self.__mark = mark

    @property
    def mark(self) -> float:
        return self.__mark

    def setMark(self, mark: float):
        if mark < 0 or mark > 10 :
            print("Improper grade, must be between 0 and 10")
            return
        self.__mark = mark

    def situation(self):
        if self.__mark > 7:
            return f"{self.name} passed!"
        else:
            return f"{self.name} didn't pass!"

aluno1 = Studen("Marina", 6.5)
print(aluno1.situation())# Reprovado
aluno1.setMark(15)# Nota inválida!
aluno1.setMark(8)
print(aluno1.mark)# 8
print(aluno1.situation())# Aprovado