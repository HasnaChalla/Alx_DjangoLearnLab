from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Book
from django.contrib.auth.decorators import permission_required
# Create your views here.


def book_list(request):
    return HttpResponse("Book list view")


def raise_exception(request):
    raise Exception("This is a test exception")


@permission_required('bookshelf.view_book', raise_exception=True)
def books(request):
    return HttpResponse("Books view")
