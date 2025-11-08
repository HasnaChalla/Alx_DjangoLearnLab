from .models import *

books = Book.objects.select_related("author").all()
for book in books:
    print(book.title, "by", book.author.name)

books = Book.objects.prefetch_related("library_set").all()
for book in books:
    print("Book:", book.title)

Librarian = Librarian.select_related("library")
print(Librarian.name, "works at", Librarian.library.name)
