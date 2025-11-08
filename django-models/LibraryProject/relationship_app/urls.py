from django.urls import path, include
from . import views
from .views import list_books
from .views import LibraryDetailView
from django.views.generic import TemplateView
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library-detail'),
]
