"""
This module is concerned with storing and retrieving books from a list.
"""
from typing import Union, Dict, List

TBook = Dict[str, Union[str, bool]]

books: List[TBook] = []


def add_book(name: str, author: str, read: bool) -> None:
    book: TBook = {'name': name, 'author': author, 'read': read}
    books.append(book)


def list_books() -> List[TBook]:
    return books


def read_book(name: str) -> None:
    bk = next((book for book in books if book['name'] == name), None)
    if bk:
        bk['read'] = True


def delete_book(name: str) -> None:
    global books
    books = [book for book in books if book['name'] != name]
