import sqlite3
from contextlib import contextmanager


class DatabaseConnection:
    """
    Context manager for SQLite database connection.

    Args:
        db_file (str): The SQLite database file.

    Example:
        with DatabaseConnection('example.db') as cursor:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            for book in books:
                print(book)
    """

    def __init__(self, db_file: str):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


@contextmanager
def database_connection(db_file: str):
    """
    Context manager for SQLite database connection.

    Args:
        db_file (str): The SQLite database file.

    Yields:
        sqlite3.Cursor: The cursor object for executing SQL commands.

    Example:
        with database_connection('example.db') as cursor:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            for book in books:
                print(book)
    """
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        yield cursor
    finally:
        conn.commit()
        conn.close()
