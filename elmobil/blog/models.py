from django.db import models

from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=56)
    date_of_create = models.DateField(auto_now_add=True)
    date_of_change = models.DateField(auto_now=True)
    autor = models.CharField(max_length=56, default='ChatGPT')
    text = models.TextField()
    tags = TaggableManager()


