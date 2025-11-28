from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db.models.functions import Coalesce
from django.db.models import Count, OuterRef, Subquery
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ArticuloForm, ComentarioForm
from .models import Articulo, Categoria, Like, Comentario
from django.contrib.auth import get_user_model
User = get_user_model()


# Pagina inicio
@login_required
def home(request):
    # Filtrado de articulos por categoría
    try:
        categoria_id = int(request.GET.get('categoria'))
    except (TypeError, ValueError):
        categoria_id = None

    articulos_generales = Articulo.objects.filter(publicado=True)
    articulos_filtrados = None

    if categoria_id:
        articulos_filtrados = articulos_generales.filter(categoria__id_categoria=categoria_id)

    # Todas las categorías
    categorias = Categoria.objects.all()

    # Nombre de la categoría activa
    categoria_nombre = None
    if categoria_id:
        categoria_obj = Categoria.objects.filter(id_categoria=categoria_id).first()
        if categoria_obj:
            categoria_nombre = categoria_obj.nombre

    # Likes del usuario
    likes_usuario = Like.objects.filter(
        usuario=request.user,
        tipo_objeto='articulo'
    ).values_list('id_objeto', flat=True)
    
    # Subquery que cuenta likes por artículo
    likes_subquery = Like.objects.filter(
        tipo_objeto='articulo',
        id_objeto=OuterRef('id_articulo')
    ).values('id_objeto').annotate(
        count=Count('id_like')
    ).values('count')
    
    # articulos populares
    articulos_populares = (
        Articulo.objects.filter(publicado=True)
        .annotate(num_likes=Coalesce(Subquery(likes_subquery), 0))
        .filter(num_likes__gt=0)
        .order_by('-num_likes', '-fecha_creacion')
    )
    
    # comments
    comentarios_recientes = Comentario.objects.filter(aprobado=True).order_by('-fecha_creacion')[:5]
    
    return render(request, 'pages/home.html', {
        'articulos': articulos_filtrados.order_by('-fecha_creacion') if articulos_filtrados else articulos_generales.order_by('-fecha_creacion'),
        'articulos_filtrados': articulos_filtrados.order_by('-fecha_creacion') if articulos_filtrados else None,
        'articulos_generales': articulos_generales.order_by('-fecha_creacion'),
        'categorias': categorias,
        'categoria_activa': categoria_id,
        'categoria_nombre': categoria_nombre,
        'likes_usuario': list(likes_usuario),
        'articulos_populares': articulos_populares,
        'comentarios_recientes': comentarios_recientes,
    })

# Pagina about  
def about_page(request):
    return render(request, 'pages/about.html')
   
# Busqueda AJAX
@login_required
def search_ajax(request):
    query = request.GET.get('q', '')
    usuarios_resultados = []
    categorias_resultados = []

    if query:
        usuarios_resultados = User.objects.filter(
            username__icontains=query
        ).exclude(rol="admin")[:5]

        categorias_resultados = Categoria.objects.filter(nombre__icontains=query)[:5]

    return render(request, 'partials/search_results.html', {
        'usuarios_resultados': usuarios_resultados,
        'categorias_resultados': categorias_resultados,
        'query': query
    })


# USER VIEWS
# Registro de usuario
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente
            messages.success(request, "Tu cuenta fue creada con éxito 🎉")
        else:
            messages.error(request, "Hubo un error al registrarte. Revisa los campos.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

# Login de usuario
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenido {user.username} 👋")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos ❌")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# info de usuario
@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado con éxito 🎉")
            return redirect('profile')
        else:
            messages.error(request, "Hubo un error al actualizar tu perfil.")
    else:
        form = CustomUserCreationForm(instance=user)

    # Publicaciones del usuario
    publicaciones = Articulo.objects.filter(autor=user).order_by('-fecha_creacion')

    return render(
        request,
        'auth/profile.html',
        {
            'form': form,
            'user': user,
            'publicaciones': publicaciones,  # 👈 ahora el template recibe las publicaciones
        }
    )

# Logout de usuario
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente 👋")
    return redirect("login")

# Perfil de otro usuario
def perfil_usuario(request, username):
    usuario = get_object_or_404(User, username=username)
    publicaciones = Articulo.objects.filter(autor=usuario).order_by('-fecha_creacion')

    return render(
        request,
        'pages/user_profile.html',
        {
            'usuario': usuario,
            'publicaciones': publicaciones,
        }
    )
    
# Get lista de usuarios (solo admin)
@user_passes_test(lambda u: u.is_superuser)
def lista_usuarios(request):
    usuarios = User.objects.all().order_by('username')
    return render(request, 'auth/lista_usuarios.html', {'usuarios': usuarios})

# Eliminar usuario (solo admin)
@user_passes_test(lambda u: u.is_superuser)
def eliminar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        usuario.delete()
        messages.success(request, f"Usuario '{usuario.username}' eliminado con éxito 🗑️")
        return redirect('lista_usuarios')
    else:
        messages.error(request, "Acción inválida ❌")
        return redirect('lista_usuarios')
# USER VIEWS END

# ARTICLE - PUBLICATION VIEWS 
# Crear publicación
@login_required
def create_publication(request):
    form = ArticuloForm()

    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            nueva_categoria = form.cleaned_data.get('nueva_categoria')

            if nueva_categoria:
                categoria_obj, created = Categoria.objects.get_or_create(nombre=nueva_categoria)
                articulo.categoria = categoria_obj
            else:
                articulo.categoria = form.cleaned_data['categoria']

            articulo.autor = request.user
            articulo.publicado = True
            articulo.save()

            messages.success(request, "Artículo creado con éxito 🎉")
            return redirect('home')
        else:
            messages.error(request, "Hubo un error al crear el artículo.")

    return render(request, 'pages/create_publication.html', {'form': form})

# Detalle de artículo
def detalle_articulo(request, id_articulo):
    articulo = get_object_or_404(Articulo, id_articulo=id_articulo)

    # Likes de artículo
    likes = Like.objects.filter(tipo_objeto='articulo', id_objeto=articulo.id_articulo)
    
    # Comentarios aprobados
    comentarios = articulo.comentarios.filter(aprobado=True).order_by('-fecha_creacion')

    # Formulario de comentario
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.usuario = request.user if request.user.is_authenticated else None
            comentario.save()
            return redirect('detalle_articulo', id_articulo=articulo.id_articulo)
    else:
        form = ComentarioForm()

    likes_usuario = []
    if request.user.is_authenticated:
        likes_usuario = Like.objects.filter(
            usuario=request.user,
            tipo_objeto='articulo'
        ).values_list('id_objeto', flat=True)

    # 2 usuarios distintos que dieron like
    usuarios_like = [like.usuario for like in likes[:2]]

    return render(request, 'pages/detalle_articulo.html', {
        'articulo': articulo,
        'likes_usuario': list(likes_usuario),
        'usuarios_like': usuarios_like,
        'comentarios': comentarios,
        'form_comentario': form,
    })
    
#Editar articulo 
@login_required
def editar_publicacion(request, articulo_id):
    articulo = get_object_or_404(Articulo, id_articulo=articulo_id, autor=request.user)

    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            articulo_editado = form.save(commit=False)
            nueva_categoria = form.cleaned_data.get('nueva_categoria')

            if nueva_categoria:
                categoria_obj, created = Categoria.objects.get_or_create(nombre=nueva_categoria)
                articulo_editado.categoria = categoria_obj
            else:
                articulo_editado.categoria = form.cleaned_data['categoria']

            articulo_editado.save()
            messages.success(request, "Artículo editado con éxito ✨")
            return redirect('profile')
        else:
            messages.error(request, "Hubo un error al editar el artículo ❌")
    else:
        form = ArticuloForm(instance=articulo)

    return render(request, 'pages/editar_publicacion.html', {'form': form, 'articulo': articulo})

# Eliminar articulo
def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id_articulo=articulo_id, autor=request.user)
    if request.method == "POST":
        articulo.delete()
        messages.success(request, "Artículo eliminado con éxito 🗑️")
        return redirect('profile')
    # Si alguien entra por GET, lo redirigimos igual
    return redirect('profile')

# Likes
@login_required
def toggle_like(request, tipo_objeto, id_objeto):
    like, created = Like.objects.get_or_create(
        usuario=request.user,
        tipo_objeto=tipo_objeto,
        id_objeto=id_objeto
    )
    if not created:
        like.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

# GET publicaciones de usuarios (solo admin)
@user_passes_test(lambda u: u.is_superuser)
def publicaciones_usuarios(request):
    publicaciones = Articulo.objects.all().order_by('-fecha_creacion')
    return render(request, 'auth/publicaciones_usuarios.html', {'publicaciones': publicaciones})

# Eliminar publicación de usuario (solo admin)
@user_passes_test(lambda u: u.is_superuser)
def eliminar_publicacion_admin(request, articulo_id):
    articulo = get_object_or_404(Articulo, id_articulo=articulo_id)
    if request.method == "POST":
        articulo.delete()
        messages.success(request, f"Publicación '{articulo.titulo}' eliminada con éxito 🗑️")
        return redirect('publicaciones_usuarios')
    else:
        messages.error(request, "Acción inválida ❌")
        return redirect('publicaciones_usuarios')
# ARTICLE - PUBLICATION VIEWS END




# Vista protegida: lista de usuarios (solo admin)
# @login_required
# def usuario_list(request):
#     from django.contrib.auth import get_user_model
#     User = get_user_model()
#     if not request.user.is_superuser:
#         messages.warning(request, "No tienes permisos para ver esta sección ⚠️")
#         return redirect('home')
#     usuarios = User.objects.all()
#     return render(request, 'auth/usuario_list.html', {'usuarios': usuarios})

# USER VIEWS ENDS