from django.db import models

# =========================
# Roles
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'roles'
    def __str__(self):
        return self.nombre
    
# =========================
# 2. Usuarios
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    contrasena_hash = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey('Rol', on_delete=models.RESTRICT, db_column='id_rol')
    activo = models.BooleanField(default=True)
    imagen_perfil = models.ImageField(upload_to='profiles/', null=True, blank=True, db_column='imagen_perfil')

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre_usuario
    
    def delete(self, using=None, keep_parents=False):
        if self.imagen_perfil:
            self.imagen_perfil.storage.delete(self.imagen_perfil.name)
        super().delete(using=using, keep_parents=keep_parents)


# =========================
# 3. Categorías
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'

    def __str__(self):
        return self.nombre


# =========================
# 4. Artículos
class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    imagen_portada = models.ImageField(upload_to='articles/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="articulos", db_column='id_autor')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'articulos'

    def __str__(self):
        return self.titulo

    def delete(self, using = None, keep_parents = False):
        self.imagen_portada.storage.delete(self.imagen_portada.name)
        super().delete()
        
# =========================
# 5. Etiquetas
class Etiqueta(models.Model):
    id_etiqueta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        managed = False
        db_table = 'etiquetas'

    def __str__(self):
        return self.nombre


# =========================
# 6. Relación Artículo - Etiqueta (N:M)
class ArticuloEtiqueta(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, db_column='id_articulo')
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, db_column='id_etiqueta')

    class Meta:
        managed = False
        db_table = 'articulo_etiqueta'
        unique_together = ('articulo', 'etiqueta')

    def __str__(self):
        return f"{self.articulo.titulo} - {self.etiqueta.nombre}"


# =========================
# 7. Comentarios
class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="comentarios", db_column='id_articulo')
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_usuario')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'comentarios'

    def __str__(self):
        return f"Comentario en {self.articulo.titulo}"

# =========================
# 8. Likes (polimórfico)
class Like(models.Model):
    id_like = models.AutoField(primary_key=True)
    TIPO_OBJETO = [
        ('articulo', 'Artículo'),
        ('comentario', 'Comentario'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    tipo_objeto = models.CharField(max_length=20, choices=TIPO_OBJETO)
    id_objeto = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'likes'
        unique_together = ('usuario', 'tipo_objeto', 'id_objeto')

    def __str__(self):
        return f"{self.usuario} dio like a {self.tipo_objeto} {self.id_objeto}"