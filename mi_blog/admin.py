from django.contrib import admin
from .models import Rol, Categoria, Articulo, Etiqueta, ArticuloEtiqueta, Comentario, Like

admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Etiqueta)
admin.site.register(ArticuloEtiqueta)
admin.site.register(Comentario)
admin.site.register(Like)
