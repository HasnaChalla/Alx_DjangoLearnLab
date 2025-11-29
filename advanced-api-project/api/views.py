from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.
# List/Create all books (GET / POST)


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Anyone can list, only authenticated can create

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

# Retrieve/Update/Delete single book (GET / PUT / DELETE)


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can update/delete; anyone can GET

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

# -- Comments --
# DRF’s generic views like ListCreateAPIView and RetrieveUpdateDestroyAPIView streamline CRUD operations.
# get_permissions() allows custom handling, e.g., restricting unsafe methods to authenticated users.
