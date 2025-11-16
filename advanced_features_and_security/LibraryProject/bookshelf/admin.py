from django.contrib import admin
from .models import Book
from .models import CustomUser
from .models import CustomUserAdmin
admin.site.register(Book)
admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
