from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from rest_framework import generics, permissions, filters
from rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# Create your views here.
# Book list view [GET]
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # filtering
    search_fields = ['title', 'author__name']  # search by book title or author name
    ordering_fields = ['title', 'publication_year']  # ordering


# Book detail view [GET]
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

# Book create view [POST]
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Book update view [PUT, PATCH]
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Book delete view [DELETE]
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]