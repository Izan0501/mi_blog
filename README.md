1. Autenticación
Register / Login / Profile
- Probar registro de usuario.
- Iniciar sesión.
- Acceder al perfil y verificar edición de datos.

2. Home
Vista principal (home)
- Se renderiza el formulario de creación de artículos al final de la página.
- Se listan los artículos publicados en cards con diseño profesional.
- Navbar con link “Publicar” lleva al formulario (#publicar).
- Filtrado de categorías:
- Al seleccionar una categoría, se muestran solo los artículos correspondientes en cards dentro del contenedor filtrado.
- Se muestra el nombre de la categoría activa.
- Próximamente:
- Se solucionará el error de recarga de página al seleccionar categoría (AJAX/Fetch para actualización dinámica).
- Scroll automático hacia la sección filtrada.
- Extras ya implementados:
- Botón “Back to Top” funcional.
- Diseño mobile-first optimizado para pantallas pequeñas.

3. Crear artículo
Formulario de creación (ArticuloForm)
- Probar inputs: título, contenido, imagen, categoría.
- Verificar estilos refinados: inputs compactos, textarea amplio, file input estilizado.
- Al enviar, se guarda el artículo y se muestra en el listado.
- Confirmar que se guarda con la categoría elegida o con nueva categoría creada.
- Próximamente:
- Mejoras visuales y funcionales en el formulario (validaciones, UX, feedback visual).

4. Categorías
Menú desplegable de categorías
- Confirmar que el artículo se guarda con la categoría elegida.
- Filtrado dinámico en cards dentro del contenedor #articulos-filtrados.
- Próximamente:
- No recarga de página al seleccionar categoría.
- Scroll automático hacia la sección filtrada.
- Mejora visual del <select> con glassmorphism y animaciones.

5. Perfil → Publicar
Desde la vista de perfil
- Probar el botón/link “Publicar artículo”.
- Confirmar que redirige al home y baja directo al formulario (#publicar).

6. Interacción en publicaciones (próximamente)
- Comentarios: los usuarios podrán dejar comentarios en cada artículo.
- Likes: sistema de “me gusta” para cada publicación.
- Barra de búsqueda: búsqueda de artículos por título, usuarios, contenido o categoría.

7. Footer (próximamente)
- Rediseño del footer con enlaces útiles, redes sociales, y estilo glassmorphism.
- Inclusión de créditos, contacto y navegación rápida.
