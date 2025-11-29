from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/',
         views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/',
         views.BookDeleteView.as_view(), name='book-delete'),
]

# -- Comments --
# /books/       [GET, POST]: List all books or create a new book.
# /books/<pk>/  [GET, PUT, PATCH, DELETE]: Retrieve, update, or delete a specific book by ID.
