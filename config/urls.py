from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_blog.urls')),  # Incluye las URLs de la aplicación mi_blog
]
