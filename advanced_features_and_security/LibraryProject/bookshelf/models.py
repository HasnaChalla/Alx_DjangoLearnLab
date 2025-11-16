from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
# Create your models here.
class CustomUser(AbstractUser):
        date_of_birth = models.DateField('date of birth', null=True, blank=True)
        profile_photo = models.ImageField('profile photo', upload_to='profiles/', null=True, blank=True)
class CustomUserManager(BaseUserManager):
      def create_user(self, date_of_birth, profile_photo, password=None, **extra_fields):
            pass
      def create_superuser(self, username, email=None, password=None, **extra_fields):
            pass