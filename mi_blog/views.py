from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ArticuloForm
from .models import Articulo

# Página de inicio
@login_required
def home(request):
    form = ArticuloForm()
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.publicado = True
            articulo.save()
            form = ArticuloForm() 
    articulos = Articulo.objects.filter(publicado=True).order_by('-fecha_creacion') 
    return render(request, 'pages/home.html', {'form': form, 'articulos': articulos})

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
    return render(request, 'auth/profile.html', {'form': form, 'user': user})

# Logout de usuario
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente 👋")
    return redirect("login")

def detalle_articulo(request, id_articulo):
    articulo = get_object_or_404(Articulo, id_articulo=id_articulo)
    return render(request, 'pages/detalle_articulo.html', {'articulo': articulo})

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