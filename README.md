1. Autenticación
Register / Login / Profile

Registro de usuario con validación de datos.

Inicio de sesión con username o email.

Acceso al perfil con posibilidad de editar datos personales.

Admin

El admin se crea con rol "admin" y tiene privilegios especiales.

La creacion debe realizarse mediante la ejecucion del script create_admin.py (python create_admin.py en la terminal).En el se encontraran los datos del admin a crear, los cuales el dueño del proyecto podra cambiarlos a gusto

Desde su perfil puede acceder a:

Lista de usuarios: ver todos los usuarios registrados y eliminarlos.

Lista de publicaciones: ver todas las publicaciones de todos los usuarios y eliminarlas.

Los usuarios con rol "admin" no aparecen en los resultados de búsqueda AJAX.

2. Home
Vista principal con:

Listado de artículos publicados en cards con diseño profesional.

Navbar con link “Publicar” que lleva al formulario de creación.

Filtrado dinámico de categorías:

Al seleccionar una categoría, se muestran solo los artículos correspondientes.

Se muestra el nombre de la categoría activa.

Implementado:

Búsqueda con AJAX:

Filtra categorías y usuarios en tiempo real.

Excluye usuarios con rol "admin".

Al hacer clic en una categoría buscada → scroll automático al contenedor #articulos-filtrados.

Al hacer clic en un perfil → redirección al perfil del usuario seleccionado con sus publicaciones.

Extras:

Botón “Back to Top” funcional.

Diseño mobile-first optimizado para pantallas pequeñas.

3. Crear artículo
Formulario de creación (ArticuloForm) con inputs:

Título, contenido, imagen, categoría.

Al enviar:

Se guarda el artículo y se muestra en el listado.

Se guarda con la categoría elegida o con nueva categoría creada.

Página dedicada /publicar/ con formulario premium.

4. Categorías
Menú desplegable de categorías.

Confirmación de que el artículo se guarda con la categoría elegida.

Filtrado dinámico en cards dentro del contenedor #articulos-filtrados.

Implementado:

Scroll automático hacia la sección filtrada al hacer clic en una categoría buscada.

5. Interacción en publicaciones
Comentarios:

Los usuarios pueden dejar comentarios en el detalle del artículo.

Likes:

Botón de corazón toggle:

Gris → sin like.

Rojo con animación → con like.

Al volver a hacer clic → se elimina el like.

En el Home:

Se muestran artículos populares ordenados por cantidad de likes.

Solo aparecen en el slider/lista los artículos con al menos un like.

En el detalle del artículo:

Corazón toggle igual que en Home.

Se muestran hasta 2 usuarios que dieron like.

Si hay más de 2 → “y otros…”.

Edición de publicaciones:

Cada usuario puede editar sus propias publicaciones desde su perfil.

Botón Editar junto a Ver y Eliminar.

Redirige a /articulo/<id>/editar/ con formulario idéntico al de creación, precargado con los datos.

Feedback visual con mensajes premium.

6. Funcionalidades Admin (nuevo)
Usuarios:

Ver todos los usuarios registrados.

Eliminar usuarios desde la lista.

Publicaciones:

Ver todas las publicaciones de todos los usuarios.

Eliminar publicaciones desde la lista.

Perfil Admin:

Links visibles solo para admin:

“Ver todos los usuarios”.

“Ver todas las publicaciones”.

7. Footer (próximamente)
Rediseño con más enlaces y redes sociales.

Inclusión de formulario para suscripción a newsletter.

Inclusión de créditos y contacto.

8. Próximamente
Sistema de mensajería: usuarios podrán interactuar entre sí por medio de la web.