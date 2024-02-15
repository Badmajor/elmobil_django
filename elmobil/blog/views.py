
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
from catalog.constants import MAX_OBJ_ON_PAGE

# Context always has arguments SITE_NAME, TITLE_FROM_INDEX
context = {
    'SITE_NAME': 'elmobil.ru',
    'TITLE_FROM_INDEX': 'Электромобили: преимущества, технологии и перспективы развития',
}


class PostsListView(ListView):
    model = Post
    paginate_by = MAX_OBJ_ON_PAGE
    paginate_orphans = 5
    ordering = '-date_of_create'


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    slug_field = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.order_by('-date_of_create')[:10]
        context['posts'] = posts
        return context


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context['slug'] = category_slug
    return render(request, template, context)
