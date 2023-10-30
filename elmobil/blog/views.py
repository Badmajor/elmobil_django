
from django.shortcuts import render

from .models import Post

# Context always has arguments SITE_NAME, TITLE_FROM_INDEX
context = {
    'SITE_NAME': 'elmobil.ru',
    'TITLE_FROM_INDEX': 'Электромобили: преимущества, технологии и перспективы развития',
}


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request, template, context)


def post_detail(request, post_slug: str):
    template = 'blog/detail.html'
    for post in Post.objects.all():
        if post.post_slug == post_slug:
            context['post'] = post
            break
    else:
        context['post'] = {'id': 777,
                           'date': 'None',
                           'author': 'None',
                           'image_path': '1.png',
                           'title': 'Еще не написали',
                           'text': 'Такого поста нет'
                           }
    context.update({
        'posts': Post.objects.all(),
    })
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context['slug'] = category_slug
    return render(request, template, context)
