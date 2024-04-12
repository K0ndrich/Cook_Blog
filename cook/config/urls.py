from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    # подключение ckeditor
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include('blog.urls')),
]
# дает возможность работать с медиа файлами при включеном Debug = True в setting.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

