# LIBRARY MANAGEMENT SYSTEM

# Define the library data structure
library = []

# Function to add a book to the library
def add_book(title, author):
    book = {
        'title': title,
        'author': author
    }
    library.append(book)
    print(f"Book '{title}' by {author} added to the library.")

# Function to view all books in the library
def view_books():
    if not library:
        print("The library is empty.")
    else:
        print("Books in the library:")
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}")

# Function to search for books by a specific author
def search_books_by_author(author):
    found_books = [book for book in library if book['author'] == author]
    if not found_books:
        print(f"No books found by author {author}.")
    else:
        print(f"Books by {author}:")
        for book in found_books:
            print(f"Title: {book['title']}")

# Function to check for duplicate books
def check_duplicates():
    titles = [book['title'] for book in library]
    duplicates = {title for title in titles if titles.count(title) > once}
    if not duplicates:
        print("No duplicate books found.")
    else:
        print("Duplicate books found:")
        for title in duplicates:
            print(title)

# Main program
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books by Author")
    print("4. Check for Duplicates")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        add_book(title, author)
    elif choice == '2':
        view_books()
    elif choice == '3':
        author = input("Enter author name: ")
        search_books_by_author(author)
    elif choice == '4':
        check_duplicates()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
