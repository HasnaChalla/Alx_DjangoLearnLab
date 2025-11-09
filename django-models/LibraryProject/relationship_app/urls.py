from django.views.generic import TemplateView
from django.urls import path, include
from . import views
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),
         name='library-detail'),
    path('login/', views.UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'),
         name='logout'
         ),
    path('register/', views.RegistrationView.as_view(), name='register'),]
