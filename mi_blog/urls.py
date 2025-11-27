from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('articulo/<int:id_articulo>/', views.detalle_articulo, name='detalle_articulo'),
    path('like/<str:tipo_objeto>/<int:id_objeto>/', views.toggle_like, name='toggle_like'),
    path('articulo/<int:articulo_id>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),
    path('perfil/<str:username>/', views.perfil_usuario, name='perfil_usuario'),
    # ruta de busqueda AJAX
    path('search-ajax/', views.search_ajax, name='search_ajax'),
]