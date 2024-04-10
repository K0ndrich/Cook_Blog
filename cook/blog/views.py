from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # self.kwargs.get("slug") - slug ето переменая, которая указываеться в URL``
        # select_related("category") подгружате таблицу, которая закреплена к полю category текущей таблици
        return Post.objects.filter(
            category__slug=self.kwargs.get("slug")
        ).select_related("category")


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    # указывает какую именно переменую из URL будем обрабатывать
    slug_url_kwarg = "post_slug"


def home(request):
    return render(request, "base.html")
