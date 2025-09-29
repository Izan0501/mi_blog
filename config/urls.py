from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_blog.urls')),  # Incluye las URLs de la aplicación mi_blog
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
