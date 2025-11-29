from django.db import models

# Author model: Stores author’s name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model: Stores title, publication year, and ForeignKey to Author


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
# -- Comments --
# The 'author' field establishes a many-to-one relationship (an author can have many books).
# related_name='books' allows Author.books.all() to return all books by that author.
