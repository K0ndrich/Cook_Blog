from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "<slug:slug>/<slug:post_slug>/",
        views.PostDetailView.as_view(),
        name="post_single",
    ),
    path("<slug:slug>/", views.PostListView.as_view(), name="post_list"),
    path("", views.HomeView.as_view(), name="home"),
    
]
