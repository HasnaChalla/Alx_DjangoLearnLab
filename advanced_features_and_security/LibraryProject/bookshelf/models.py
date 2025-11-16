from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
# Create your models here.
class CustomUser(AbstractUser):
        date_of_birth = models.DateField('date of birth', null=True, blank=True)
        profile_photo = models.ImageField('profile photo', upload_to='profiles/', null=True, blank=True)