<!-- @format -->

from bookshelf.models import Book

# Retrieve the book by ID

book = Book.objects.get(title="Animal farm")

# Display the retrieved book

print(f"Retrieved Book is: {book.title} by author: {book.author}, published {book.publication_year}")
