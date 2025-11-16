from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# Extend the User Model with a UserProfile


class UserProfile(models.Model):
    class UserProfile(models.Model):
        ROLE_CHOICES = [
            ('Admin', 'Admin'),
            ('Librarian', 'Librarian'),
            ('Member', 'Member'),
        ]
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

        def __str__(self):
            return f"{self.user.username} - {self.role}"
# Signal to create or update UserProfile whenever User is created
class CustomUser(AbstractUser):
        date_of_birth = models.DateField('date of birth'),
        profile_photo = models.ImageField('profile photo'),
        

@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
