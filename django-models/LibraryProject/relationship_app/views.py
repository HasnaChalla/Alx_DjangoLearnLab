from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all books in this library using the ManyToManyField relationship
        context['books'] = self.object.books.all()
        return context
# === AUTHENTICATION VIEWS ===


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')


# Login Django's built-in class-based view
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout Django's built-in class-based view


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect after logout
