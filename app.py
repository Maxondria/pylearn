import random
from urllib.parse import urlparse
from utils import database


user_prompt = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def menu():
    user_input = input(user_prompt)

    while user_input != 'q':
        if user_input == 'a':
            promt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        user_input = input(user_prompt)


def promt_add_book():
    input_data = input(
        "Enter the book name, author, and read status (True/False) separated by commas: ")

    parts = input_data.split(',')
    if len(parts) != 3:
        print("Invalid input. Please ensure to include name, author, and read status separated by commas.")
        return

    name, author, read_str = parts
    read = read_str.strip().lower() in ['true', '1', 't', 'yes', 'y']

    database.add_book(name, author, read)


def list_books():
    books = database.list_books()
    for book in books:
        print(
            f"{book['name']} by {book['author']}, read: {'Yes' if book['read'] else 'No'}")


def prompt_read_book():
    name = input("Enter the name of the book you just finished reading: ")
    database.read_book(name)


def prompt_delete_book():
    name = input("Enter the name of the book you want to delete: ")
    database.delete_book(name)


menu()
