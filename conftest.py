import pytest

from models import Book, Library


@pytest.fixture(scope="session")
def book() -> Book:
    harry_potter = Book(name="Harry Potter", name_author="Joanne Rowling")
    return harry_potter


@pytest.fixture(scope="session")
def library() -> Library:
    library = Library(name="KSD")
    return library

