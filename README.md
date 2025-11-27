1. Autenticación
Register / Login / Profile

Probar registro de usuario.

Iniciar sesión.

Acceder al perfil y verificar edición de datos.

2. Home
Vista principal (home)

Se renderiza el formulario de creación de artículos al final de la página.

Se listan los artículos publicados en cards con diseño profesional.

Navbar con link “Publicar” lleva al formulario (#publicar).

Filtrado de categorías:

Al seleccionar una categoría, se muestran solo los artículos correspondientes en cards dentro del contenedor filtrado.

Se muestra el nombre de la categoría activa.

Implementado:

Búsqueda con AJAX que permite filtrar categorías y usuarios en tiempo real desde la barra de búsqueda.

Al hacer clic en una categoría buscada, la página baja automáticamente hasta el contenedor #articulos-filtrados donde se muestran sus artículos y próximamente se podrá navegar hacia el perfil de un usuario que mostrará sus publicaciones realizadas.

Extras ya implementados:

Botón “Back to Top” funcional.

Diseño mobile-first optimizado para pantallas pequeñas.

3. Crear artículo
Formulario de creación (ArticuloForm)

Probar inputs: título, contenido, imagen, categoría.

Verificar estilos refinados: inputs compactos, textarea amplio, file input estilizado.

Al enviar, se guarda el artículo y se muestra en el listado.

Confirmar que se guarda con la categoría elegida o con nueva categoría creada.

Próximamente:

Mejoras visuales y funcionales en el formulario (validaciones, UX, feedback visual).

4. Categorías
Menú desplegable de categorías

Confirmar que el artículo se guarda con la categoría elegida.

Filtrado dinámico en cards dentro del contenedor #articulos-filtrados.

Implementado:

Scroll automático hacia la sección filtrada al hacer clic en una categoría buscada.

5. Interacción en publicaciones
Comentarios (implementado)
Los usuarios pueden dejar comentarios en cada artículo a traves de un input seguido de clickear en el boton "comentar".

Likes (implementado)
Se agregó un sistema de “me gusta” para cada publicación.

El botón de corazón funciona como toggle:

Si el artículo no tiene like del usuario → el corazón aparece gris.

Al hacer clic → se guarda el like, el corazón se vuelve rojo con animación estilo Instagram.

Si el artículo ya tiene like del usuario → el corazón aparece rojo.

Al hacer clic nuevamente → se elimina el like y el corazón vuelve a gris.

En el Home:

Se muestran los artículos populares ordenados por cantidad de likes.

Solo aparecen en el slider/lista los artículos que tienen al menos un like.

En el detalle del artículo:

El corazón también funciona como toggle (dar o quitar like).

Al lado del corazón se muestran hasta 2 usuarios que dieron like a ese artículo.

Si hay más de 2 usuarios, se indica con “y otros…”.

Todo integrado con estilos glassmorphism y animaciones de pulso para reforzar la experiencia visual.

6. Footer (próximamente)
Rediseño del footer con enlaces útiles, redes sociales, y estilo glassmorphism.

Inclusión de créditos, contacto y navegación rápida.