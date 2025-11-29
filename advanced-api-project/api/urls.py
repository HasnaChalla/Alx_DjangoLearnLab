from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]

# -- Comments --
# /books/       [GET, POST]: List all books or create a new book.
# /books/<pk>/  [GET, PUT, PATCH, DELETE]: Retrieve, update, or delete a specific book by ID.