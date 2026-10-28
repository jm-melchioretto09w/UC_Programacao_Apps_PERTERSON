class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.maxPages = pages
        self.pagesRead: int = 0

    def read(self, pages: int):
        self.pagesRead += pages
        if self.pagesRead > self.maxPages:
            self.pagesRead = self.maxPages

    def percentageRead(self) -> float:
        return self.pagesRead * 100 / self.maxPages

    def pagesLeft(self) -> int:
        return self.maxPages - self.pagesRead

    def finished(self):
        return self.maxPages == self.pagesRead

livro1 = Book("Poeira em alto mar", "Paradoxo", 300)
livro1.read(68)
print(f"{livro1.percentageRead()}%")
print(livro1.pagesLeft())
print(livro1.finished())