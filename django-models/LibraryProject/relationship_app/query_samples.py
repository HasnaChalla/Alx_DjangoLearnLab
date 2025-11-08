from .models import *

# Query all books by a specific author.

books = Book.objects.select_related("author").all()
for book in books:
    print(book.title, "by", book.author.name)

# List all books in a library.

library_name = "Central Library"  # Example library name
library = Library.objects.get(name=library_name)
library_books = library.books.all()
for book in library_books:
    print("Book:", book.title)

# Retrieve the librarian for a library.

Librarian = Librarian.select_related("library")
print(Librarian.name, "works at", Librarian.library.name)
