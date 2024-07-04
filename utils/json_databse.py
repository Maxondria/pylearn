import json


db_file = 'books.json'

__all__ = ['add_book', 'list_books', 'read_book',
           'delete_book', 'create_book_table']


def create_book_table() -> None:
    with open(db_file, 'w') as file:
        json.dump([], file)


def _save_books(books: list[dict]) -> None:
    with open(db_file, 'w') as file:
        json.dump(books, file)


def add_book(name: str, author: str, read: bool) -> None:
    books = list_books()
    books.append({'name': name, 'author': author, 'read': read})
    _save_books(books)


def list_books() -> list[dict]:
    with open(db_file, 'r') as file:
        return json.load(file)


def read_book(name: str) -> None:
    books = list_books()
    book = next((book for book in books if book['name'] == name), None)
    if book:
        book['read'] = True
        _save_books(books)


def delete_book(name: str) -> None:
    books = list_books()
    books = [book for book in books if book['name'] != name]
    _save_books(books)
