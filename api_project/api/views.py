from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Book 
from .serializers import BookSerializer 
# Create your views here.
class BookList(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]