<!-- @format -->

from bookshelf.models import Book

# Retrieve the book by ID

book = Book.objects.get(title="1984")

# Display the retrieved book

print(f"Retrieved Book is: {book.title} by author: {book.author}, published {book.publication_year}")
