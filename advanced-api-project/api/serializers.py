from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    # Serializes all Book fields
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation: publication_year must not be in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer dynamically serializes all books for an author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

# -- Comments --
# BookSerializer validates input and ensures correct serialization of Book objects.
# AuthorSerializer nests BookSerializer under 'books', leveraging the related_name in Book.author.
# This setup lets you serialize an author along with all their books in one API call.