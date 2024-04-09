from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # self.kwargs.get("slug") - slug ето переменая, которая указываеться в URL``
        return Post.objects.filter(category__slug=self.kwargs.get("slug"))


def home(request):
    return render(request, "base.html")
