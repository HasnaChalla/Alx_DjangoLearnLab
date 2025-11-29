from .models import Book, Author
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class BookAPITests(APITestCase):
    def setUp(self):  # Create test user and authenticate as needed
        # Create an user
        self.user = User.objects.create_user(
            username="testuser", password="pass1234")
        # Create an author
        self.author = Author.objects.create(name="Amin Maalouf")
        # Create a book
        self.book = Book.objects.create(
            title='Leo Africanus',
            publication_year=1986,
            Author=self.author)
        # Url to test
        self.list_url = '/api/books/'

    def test_create_book_authenticated(self):
        """Test if if the logged-in user can create a book"""
        self.client.login(username="testuser", password="pass1234")
        url = 'books/create/'
        data = {
            "title": "The Silmarillion",
            "publication_year": 1977,
            "author": self.author.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if the book exist in the database
        self.assertEqual(Book.objects.get(
            title="The Silmarillion").title, "The Silmarillion")

    def test_book_create_unauthenticated(self):
        url = '/api/books/create/'
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2000,
            "author": self.author.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_book_update_authenticated(self):
        self.client.login(username="testuser", password="pass1234")
        url = 'books/update/<int:pk>/'

        new_title = "The Hobbit: An Unexpected Journey"
        response = self.client.put(url, {
            "title": new_title,
            "publication_year": 1937,
            "author": self.author.pk
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, new_title)

    def test_delete_book(self):

        self.client.login(username="testuser", password="pass1234")

        url = ('/api/books/delete/{self.book.pk}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        # Filter test by title
        url = ("books/")
        response = self.client.get(
            url, {"title": "The Hobbit: An Unexpected Journey"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"],
                         "The Hobbit: An Unexpected Journey")
