import uuid


class Book:
    def __init__(self, name_author: str, name: str):
        self.name_author: str = name_author
        self.name: str = name
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return f"<Book {self.name} - {self.inn}>"


class Library:
    def __init__(
        self,
        name: str,
    ):
        self.name: str = name
        self.name: name
        self.list_book: list[Book] = []

    def add_book(self, book: Book):
        self.list_book.append(book)

    def delete_book(self, book_inn):
        for book in self.list_book:
            if book.inn == book_inn:
                self.list_book.remove(book)
                break
