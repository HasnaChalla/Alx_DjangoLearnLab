from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from .models import Library
from .models import Book
from .models import UserProfile

# === BOOK LIST VIEW ===


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


class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

    dummy_form = UserCreationForm()


register = RegistrationView.as_view()

# Login Django's built-in class-based view


class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout Django's built-in class-based view


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect after logout

# --- Role check functions ---


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Views ---


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
