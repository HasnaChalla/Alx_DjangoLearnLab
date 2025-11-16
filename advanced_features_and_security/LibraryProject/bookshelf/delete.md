<!-- @format -->

from bookshelf.models import Book

# Retrieve the book to delete

book = Book.objects.get(title="Animal farm - Classic Edition")

# Display the book before deletion

print(f"Book to delete: Title: {book.title}, by author: {book.author}, published {book.publication_year}")

# Delete the book

book.delete()
print("\nBook deleted successfully!")

# Verify deletion by trying to retrieve all books

all_books = Book.objects.all()
print(f"Remaining books in database: {all_books}")
