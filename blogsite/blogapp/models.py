from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 250)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post ,related_name = "comments", on_delete = models.CASCADE)
    name = models.CharField(max_length= 100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True) 

    def get_absolute_url(self):
        return reverse('home')

class Subscriber(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()