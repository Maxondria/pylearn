
from utils.database_connection import database_connection

db_file = "sqlite.db"


def create_book(name: str, author: str, read: bool) -> None:
    """
    Creates a new book record in the books table in an SQLite database.

    Args:
        name (str): The name of the book.
        author (str): The author of the book.
        read (bool): The read status of the book.
    """
    with database_connection(db_file) as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (name TEXT PRIMARY KEY, author TEXT, read BOOLEAN)")

        cursor.execute(
            "INSERT INTO books (name, author, read) VALUES (?, ?, ?)", (name, author, read))


def list_books():
    """
    Retrieves all book records from the books table in an SQLite database.

    Returns:
        list[dict]: A list of dictionaries, each representing a book with keys 'name', 'author', and 'read'.
    """
    with database_connection(db_file) as cursor:
        cursor.execute("SELECT * FROM books")
        books = [{"name": row[0], "author": row[1], "read": row[2]}
                 for row in cursor.fetchall()]
    return books


def read_book(name: str) -> None:
    """
    Marks a book as read in the books table in an SQLite database based on the book's name.

    Args:
        name (str): The name of the book to be marked as read.
    """
    with database_connection(db_file) as cursor:
        cursor.execute("SELECT 1 FROM books WHERE name = ?", (name,))
        book = cursor.fetchone()

        if book:
            cursor.execute(
                "UPDATE books SET read = ? WHERE name = ?", (True, name))


def delete_book(name: str, db_file: str = 'books.db') -> None:
    """
    Removes a book record from the books table in an SQLite database based on the book's name.

    Args:
        name (str): The name of the book to be deleted from the database.
        db_file (str): The SQLite database file. Default is 'books.db'.
    """
    with database_connection(db_file) as cursor:
        cursor.execute("DELETE FROM books WHERE name = ?", (name,))
