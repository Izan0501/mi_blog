from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Usuarios
class CustomUser(AbstractUser):
    rol = models.CharField(max_length=50, default='usuario')
    imagen_perfil = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    class Meta:
        db_table = 'usuarios'
        
    def __str__(self):
        return self.username
    
# Roles
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.nombre

# Categorias
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.nombre

# Articulos
class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    imagen_portada = models.ImageField(upload_to='articles/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articulos")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'articulos'

    def __str__(self):
        return self.titulo
    
class Etiqueta(models.Model):
    id_etiqueta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'etiquetas'

    def __str__(self):
        return self.nombre

# Relación Artículo - Etiqueta (N:M)
class ArticuloEtiqueta(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'articulo_etiqueta'
        unique_together = ('articulo', 'etiqueta')

    def __str__(self):
        return f"{self.articulo.titulo} - {self.etiqueta.nombre}"

# Mensajes
class Mensaje(models.Model):
    remitente = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # 👈 referencia correcta
        on_delete=models.CASCADE,
        related_name="mensajes_enviados"
    )
    destinatario = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # 👈 referencia correcta
        on_delete=models.CASCADE,
        related_name="mensajes_recibidos"
    )
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"De {self.remitente} a {self.destinatario} - {self.contenido[:30]}"
# Comentarios
class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="comentarios")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=True)

    class Meta:
        db_table = 'comentarios'

    def __str__(self):
        return f"Comentario en {self.articulo.titulo}"

# Likes
class Like(models.Model):
    id_like = models.AutoField(primary_key=True)
    TIPO_OBJETO = [
        ('articulo', 'Artículo'),
        ('comentario', 'Comentario'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo_objeto = models.CharField(max_length=20, choices=TIPO_OBJETO)
    id_objeto = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'likes'
        unique_together = ('usuario', 'tipo_objeto', 'id_objeto')

    def __str__(self):
        return f"{self.usuario} dio like a {self.tipo_objeto} {self.id_objeto}"