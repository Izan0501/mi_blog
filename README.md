1. Autenticación
Registro/Login/Perfil

Registro: Validación de datos, imagen de perfil opcional, rol por defecto “usuario”.

Login: Con username o email.

Perfil: Visualización y edición de datos personales, avatar premium.

Admin

Creación: Se crea con rol “admin” mediante python create_admin.py, con datos configurables por el dueño del proyecto.

Privilegios: Acceso a listas globales de usuarios y publicaciones, con capacidad de eliminación.

Búsqueda AJAX: Usuarios con rol “admin” no aparecen en resultados.

2. Home
Listado principal: Cards de artículos con diseño premium.

Navbar: Link “Publicar” hacia el formulario de creación.

Filtrado dinámico de categorías

Selección: Muestra artículos de la categoría seleccionada, indicando categoría activa.

Búsqueda AJAX

Usuarios y categorías: Filtra en tiempo real.

Exclusión: Omite usuarios con rol “admin”.

Acciones: Click en categoría → scroll a #articulos-filtrados; click en perfil → redirección al perfil del usuario con sus publicaciones.

Extras

Back to Top: Botón funcional.

Mobile-first: Diseño optimizado.

3. Crear artículo
Formulario (ArticuloForm): Título, contenido, imagen, categoría.

Guardado:

Publicación: Se guarda y aparece en el listado.

Categoría: Usa existente o crea nueva si corresponde.

Página dedicada: /publicar/ con interfaz premium.

4. Categorías
Menú desplegable: Selección clara de categorías.

Confirmación: Los artículos se guardan con la categoría elegida.

Filtrado dinámico: Cards en #articulos-filtrados.

Scroll automático: Al hacer clic en una categoría buscada.

5. Interacción en publicaciones
Comentarios: En detalle del artículo.

Likes (toggle):

Estados: Gris (sin like), rojo animado (con like).

Comportamiento: Segundo click elimina like.

Home:

Populares: Orden por cantidad de likes.

Regla: Solo artículos con al menos un like aparecen en slider/lista.

Detalle del artículo:

Toggle corazón: Igual que Home.

Visualización: Hasta 2 usuarios que dieron like, “y otros…” si hay más.

Edición de publicaciones:

Acceso: Desde el perfil del autor.

Flujo: “Editar” junto a “Ver” y “Eliminar”; redirige a /articulo/<id>/editar/ con formulario precargado.

Feedback: Mensajes visuales premium.

6. Funcionalidades admin
Usuarios:

Listado global: Ver y eliminar usuarios.

Publicaciones:

Listado global: Ver y eliminar publicaciones.

Perfil admin:

Links exclusivos: “Ver todos los usuarios”, “Ver todas las publicaciones”.

7. Footer (próximamente)
Rediseño: Más enlaces y redes sociales.

Newsletter: Formulario de suscripción.

Créditos y contacto: Inclusión destacada.

8. Sistema de mensajería entre usuarios
Modelo:

Mensaje:

Campos: remitente, destinatario, contenido, fecha_envio, leido.

Relaciones: Usa settings.AUTH_USER_MODEL para compatibilidad con CustomUser.

Bandeja de entrada (conversaciones únicas):

Vista: Muestra una tarjeta por chat (último mensaje) entre el usuario y cada contacto.

Lectura: Al entrar, marca como leídos los mensajes no leídos del usuario, reseteando el contador del navbar.

Navegación: Click en tarjeta → detalle_mensaje con el otro usuario (nunca abre chat consigo mismo).

Chat (detalle_mensaje):

Vista: Conversación completa entre dos usuarios (remitente/destinatario), ordenada por fecha.

Marcado: Al abrir, marca como leídos los mensajes del otro usuario hacia el actual.

Envío inline: Form para enviar mensajes dentro del chat, sin redirigir a formularios externos.

Header premium: Avatar + nombre del contacto; opcionalmente clickeable hacia su perfil.

Botón “Enviar mensaje” en perfil de usuario:

Condición: Visible si el usuario autenticado no es el mismo perfil.

Acción: Redirige a detalle_mensaje con el usuario de ese perfil.

Navbar (badge de notificaciones):

Contador: Muestra badge con cantidad de mensajes no leídos sobre el nombre del usuario.

Cálculo: Se obtiene en la vista o via context processor; no se realizan .filter(...) con argumentos en el template.

Reset: El badge desaparece al entrar a la bandeja (mensajes marcados como leídos).

Exclusiones:

Admins: Excluidos como destinatarios en envío de mensajes; no aparecen en resultados AJAX.

Rutas:

Bandeja: /mensajes/ → lista de chats (últimos mensajes).

Chat: /mensajes/<user_id>/ → conversación con el usuario dado.

Plantillas premium:

Bandeja: Tarjetas con avatar, nombre, último mensaje, fecha y estado no leído.

Chat: Burbujas enviadas y recibidas, scroll, form de envío inline; header con avatar+nombre.

Comportamiento del link en bandeja:

Si el último lo enviaste vos: Link a chat con destinatario.

Si lo recibiste: Link a chat con remitente.

Opt-in realtime (futuro):

Canales/WebSockets: Posibilidad de notificaciones instantáneas y actualización de chat en vivo.

9. Próximamente
Sistema de mensajería (extensiones):

Realtime: Notificaciones y chat en tiempo real.

Estados de entrega/lectura por mensaje.

