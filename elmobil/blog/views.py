from django.shortcuts import render

from .posts_list import posts


def index(request):
    template = 'blog/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, id: int):
    template = 'blog/detail.html'
    for post in posts:
        if post.get('id') == id:
            context = {'post': post}
            break
    else:
        context = {'post': {'id': id,
                            'date': 'None',
                            'author': 'None',
                            'title': 'Еще не написали',
                            'text': 'Такого поста нет'
                            }}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'slug': category_slug}
    return render(request, template, context)
