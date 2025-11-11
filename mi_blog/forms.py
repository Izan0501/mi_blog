from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Articulo

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        exclude = ('rol', 'is_staff', 'is_active', 'is_superuser')
        fields = ('username', 'email', 'imagen_perfil')
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta: 
        model = CustomUser
        fields = ('username', 'password')
        
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'imagen_portada', 'categoria']