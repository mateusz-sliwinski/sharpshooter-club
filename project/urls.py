"""sharpshooter_club URL Configuration."""
# Django
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
