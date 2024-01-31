class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def display_info(self):
        super().display_info()
        print(f"File Format: {self.file_format}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_all_books(self):
        for book in self.books:
            book.display_info()

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

# Create instances
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
ebook1 = EBook("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", "PDF")

# Create a library instance
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(ebook1)

# Display all books in the library
print("All Books in the Library:")
library.display_all_books()

# Search for a book by title
searched_book_title = "The Great Gatsby"
searched_book = library.search_book_by_title(searched_book_title)
if searched_book:
    print(f"\nBook found by title '{searched_book_title}':")
    searched_book.display_info()
else:
    print(f"\nBook with title '{searched_book_title}' not found.")