<!-- @format -->

from bookshelf.models import Book

# Retrieve the book to update

book = Book.objects.get(title="Animal farm")

# Display original title

print(f"Original Title: {book.title}")

# Update the title

book.title = "Nineteen Eighty-Four"
book.save()

# Display updated title

print(f"Updated Title: {book.title}")

# Verify the update by retrieving again

book = Book.objects.get(Title :"Nineteen Eighty-Four")
print(f"\nVerified Updated Book: {book.title} by author: {book.author}, published {book.publication_year}.")
