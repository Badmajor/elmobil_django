from django.contrib import admin

from .models import Category, Autor, Tags, Post

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Autor)
admin.site.register(Tags)
