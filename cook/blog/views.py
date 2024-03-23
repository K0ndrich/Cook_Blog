from django.shortcuts import render
from django.views.generic import ListView


class PostListView(ListView):
    pass


def home(request):
    return render(
        request,
        "base.html",
    )
