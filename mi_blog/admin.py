from django.contrib import admin
from .models import Rol, Usuario, Categoria, Articulo, Etiqueta, ArticuloEtiqueta, Comentario, Like
from django.utils.html import format_html

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'email', 'rol', 'activo', 'mostrar_imagen')

    def mostrar_imagen(self, obj):
        if obj.imagen_perfil:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.imagen_perfil.url)
        return "Sin imagen"
    mostrar_imagen.short_description = "Imagen de perfil"


admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Etiqueta)
admin.site.register(ArticuloEtiqueta)
admin.site.register(Comentario)
admin.site.register(Like)
