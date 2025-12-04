from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('publicar/', views.create_publication, name='create_publication'),
    path('articulo/<int:id_articulo>/', views.detalle_articulo, name='detalle_articulo'),
    path('articulo/<int:articulo_id>/editar/', views.editar_publicacion, name='editar_publicacion'),
    path('like/<str:tipo_objeto>/<int:id_objeto>/', views.toggle_like, name='toggle_like'),
    path('articulo/<int:articulo_id>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),
    path('perfil/<str:username>/', views.perfil_usuario, name='perfil_usuario'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('publicaciones/', views.publicaciones_usuarios, name='publicaciones_usuarios'),
    path('publicaciones/eliminar/<int:articulo_id>/', views.eliminar_publicacion_admin, name='eliminar_publicacion_admin'),
    path('mensajes/', views.bandeja_entrada, name='bandeja_entrada'),
    path('mensajes/enviar/', views.enviar_mensaje, name='enviar_mensaje'),


    # ruta de busqueda AJAX
    path('search-ajax/', views.search_ajax, name='search_ajax'),
]