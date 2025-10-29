from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm

# render home page
def home(request):
    return render(request, 'pages/home.html')

# render users list
def user_list(request):
    users = Usuario.objects.all()
    return render(request, 'pages/users/user_list.html', {'users': users})

# render users detail
def user_detail(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    return render(request, 'pages/users/user_detail.html', {'user': user})

# render create user
def user_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UsuarioForm()
    return render(request, 'pages/users/user_create.html', {'form': form})

# render user update - edit
def user_update(request, pk):
    user = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UsuarioForm(instance=user)
    return render(request, 'pages/users/user_update.html', {'form': form})

# render user delete
def user_delete(request, pk):
    user =  get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'pages/users/user_delete.html', {'user' : user})