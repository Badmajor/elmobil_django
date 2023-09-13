from django.shortcuts import render

from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, post_slug: str):
    template = 'blog/detail.html'
    posts = Post.objects.all()
    for post in posts:
        if post.post_slug == post_slug:
            context = {'post': post}
            break
    else:
        context = {'post': {'id': 777,
                            'date': 'None',
                            'author': 'None',
                            'image_path': '1.png',
                            'title': 'Еще не написали',
                            'text': 'Такого поста нет'
                            }}
    context['posts'] = posts
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'slug': category_slug}
    return render(request, template, context)
