from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Articulo, Comentario

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
    nueva_categoria = forms.CharField(
        required=False,
        label="Nueva categoría",
        widget=forms.TextInput(attrs={'placeholder': 'Crear nueva categoría'})
    )
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'imagen_portada', 'categoria']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escribe un comentario...',
                'class': 'comentario-input'
            }),
        }
        labels = {
            'contenido': ''
        }