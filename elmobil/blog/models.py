from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name


class Autor(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=56)
    post_url = models.URLField(default=title, max_length=75)
    date_of_create = models.DateField(auto_now_add=True)
    date_of_change = models.DateField(auto_now=True)
    autor = models.ForeignKey(Autor, default='autor', on_delete=models.PROTECT)
    text = models.TextField()
    views_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title
