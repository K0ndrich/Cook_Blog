from django.db import models

# берем стандартную модель пользователя
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    # создаеться дочеряняя колонка, которая являеться екзепляром текущей модели
    parent = TreeForeignKey(
        "self",
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    # устанавливаем сортировка order_by п имени
    class MPTTMeta:
        order_insertion_by = ["name"]


# содержит теги для постов
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


# внутри себя содержит однин целый пост
class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # поле хранит изображение , upload_to указывает куда будет ложиться изображение после загрузки из сайта
    image = models.ImageField(upload_to="articles/")
    text = models.TextField()
    category = models.ForeignKey(
        Category, related_name="post", on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(Tag, related_name="post")
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, default="")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug}
        )

    # возвращает все рецепты указаного поста
    def get_recipes(self):
        return self.recipes.all()


# блок с рецептом по середине поста
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, related_name="recipes", null=True, blank=True
    )


# блок с отправкой коментариев внизу поста
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    web_site = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
