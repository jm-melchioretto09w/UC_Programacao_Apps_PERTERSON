class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.pagesRead: int = 0

    def read(self, pages: int):
        self.pagesRead += pages
        if self.pagesRead > self.pages:
            self.pagesRead = self.pages

    def percentageRead(self) -> float:
        return self.pagesRead * 100 / self.pages

    def pagesLeft(self) -> int:
        return self.pages - self.pagesRead

    def finished(self):
        if self.pagesRead != self.pages:
            return False
        return True

livro1 = Book("Dom Casmurro", "Machado de Assis", 256)
livro1.read(64)
print(livro1.percentageRead())
print(livro1.pagesLeft())
print(livro1.finished())