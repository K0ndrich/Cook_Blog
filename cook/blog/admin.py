from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models


# позволяет редакторивать в родительской модели и дочернюю модель
class RecipeInLine(admin.StackedInline):
    model = models.Recipe
    # указываем количество дополнительных форм в базовой модели для заполенения
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    # указывает кокие колонки будут вывовить в базе Post , нужно прописывать регистрацию для етого класса
    list_display = ["title", "category", "create_at", "id", "author"]
    # подключаем редактирование дочерней модели
    inlines = [RecipeInLine]


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


# покдлючаем admin class чтоб отображаться вложенные внутрь категории
admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)

# можно регистрировать по другому
# admin.site.register(models.Recipe , RecipeAdmin)
# admin.site.register(models.Post, PostAdmin)
