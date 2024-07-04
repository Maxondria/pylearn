db_file = 'books.csv'

# __all__ = ['add_book', 'list_books', 'read_book',
#            'delete_book', 'create_book_table']


def create_book_table() -> None:
    with open(db_file, 'w'):
        pass


def add_book(name: str, author: str, read: bool) -> None:
    with open(db_file, 'a') as file:
        file.write(f"{name},{author},{read}\n")


def list_books() -> list[dict]:
    create_book_table()
    with open(db_file, 'r') as file:
        book_lines = [line.strip().split(',') for line in file.readlines()]

        return [{'name': name, 'author': author, 'read': read}
                for name, author, read in book_lines]


def read_book(name: str) -> None:
    books = list_books()

    book = next((book for book in books if book['name'] == name), None)

    if book:
        book['read'] = True
    _save_books(books)


def _save_books(books: list[dict]) -> None:
    with open(db_file, 'w') as file:
        lines = [f"{book['name']},{book['author']},{book['read']}"
                 for book in books]
        file.writelines(lines)


def delete_book(name: str) -> None:
    books = list_books()
    books = [book for book in books if book['name'] != name]
    _save_books(books)
