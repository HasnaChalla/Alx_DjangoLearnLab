from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



class Tag(models.Model):
    name  = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title