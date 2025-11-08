<!-- @format -->

from bookshelf.models import Book

# Create a new Book instance

book = Book.objects.create(
title="1984",
author="George Orwell",
publication_year=1949
)

# Display the created book

print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
