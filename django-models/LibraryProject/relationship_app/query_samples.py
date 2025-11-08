from .models import *

# Query all books by a specific author.

author_name = "J.K. Rowling"  # Example author name
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
for book in books:
    print(book.title, "by", author.name)

# List all books in a library.

library_name = "Central Library"  # Example library name
library = Library.objects.get(name=library_name)
library_books = library.books.all()
for book in library_books:
    print("Book:", book.title)

# Retrieve the librarian for a library.
library_name = "Central Library"
try:
    # First get the library
    library = Library.objects.get(name=library_name)
    # Then get the librarian for this library using select_related for efficiency
    librarian = Librarian.objects.select_related(
        'library').get(library=library)
    print(f"{librarian.name} works at {librarian.library.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found")
except Librarian.DoesNotExist:
    print(f"No librarian found for {library_name}")
