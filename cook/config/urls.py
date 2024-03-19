from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
]
# дает возможность работать с медиа файлами при включеном Debug = True в setting.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
