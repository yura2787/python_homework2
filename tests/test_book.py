class TestBook:

    def test_book(
        self,
        book,
    ):
        assert book.name
        assert book.name_author
        assert book.inn

    def test_name(self, book):
        assert book.name == "Harry Potter"
        assert book.name_author == "Joanne Rowling"


class TestLibrary:
    def test_book_in_library(self, book, library):
        library.add_book(book)
        assert book in library.list_book

    def test_library_book(self, book):
        assert book.name == "Harry Potter"

    def test_library(self, library):
        assert library.name == "KSD"

    def test_delete_book(self, book, library):
        assert book in library.list_book
        library.delete_book(book_inn=book.inn)
        assert book not in library.list_book
