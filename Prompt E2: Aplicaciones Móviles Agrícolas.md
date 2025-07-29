Especificación de Aplicación Móvil: AgroFinca Conectada

Resumen Ejecutivo

Este documento detalla las especificaciones técnicas y funcionales para el desarrollo de "AgroFinca Conectada", una aplicación móvil nativa para Android e iOS. La aplicación está diseñada para digitalizar y optimizar las operaciones de campo en las fincas de café de Guatemala, con una integración robusta y en tiempo real con el sistema ERPNext. El objetivo es mejorar la eficiencia, la toma de decisiones y la trazabilidad en toda la cadena de producción, desde la siembra hasta la cosecha.  

1. Funcionalidades Core

El núcleo de la aplicación se construirá sobre una arquitectura "offline-first" para garantizar la máxima fiabilidad en entornos rurales con conectividad intermitente.  

Funcionalidad	Descripción Técnica
Registro de Actividades	

Los usuarios (trabajadores de campo, supervisores) podrán registrar actividades diarias (siembra, poda, fertilización, cosecha) a través de formularios optimizados. Cada registro llevará una marca de tiempo automática.  

Captura de Fotos con GPS	

La cámara integrada permitirá tomar fotografías y adjuntarlas a los registros de actividad. Cada foto capturará y almacenará automáticamente metadatos EXIF, incluyendo coordenadas GPS, dirección (brújula) y fecha/hora.  Esta función es crucial para la verificación de tareas, el monitoreo de plagas y la documentación del progreso del cultivo.  

Sincronización Bidireccional	

La aplicación mantendrá los datos idénticos tanto en el dispositivo móvil como en el servidor ERPNext.  Los cambios realizados en la app se reflejarán en el ERP y viceversa. Esto asegura una única fuente de verdad para todos los usuarios, desde el campo hasta la oficina.  

Modo Offline Robusto	

La aplicación será completamente funcional sin conexión a internet. Todos los datos y fotos se guardarán en una base de datos local (ej. Room en Android, CoreData en iOS).  Un gestor de tareas en segundo plano (ej. WorkManager) se encargará de poner en cola las subidas y sincronizará automáticamente los datos cuando se restablezca la conexión.  Se implementará una estrategia de resolución de conflictos basada en la marca de tiempo (  

	

lastModified) para gestionar ediciones concurrentes.  

Notificaciones Push	

Se utilizará un servicio como Firebase Cloud Messaging para enviar alertas en tiempo real a los usuarios. Las notificaciones pueden incluir asignaciones de nuevas tareas, alertas de plagas, recordatorios de riego o fluctuaciones en los precios del mercado.  

2. Interfaces de Usuario (UI/UX)

El diseño se centrará en la usabilidad en condiciones de campo adversas y para usuarios con diferentes niveles de alfabetización digital.  

Característica	Especificación de Diseño
Diseño para Campo	

Se utilizarán botones grandes y bien espaciados para facilitar la interacción táctil, incluso con guantes o manos sucias.  La navegación será minimalista, evitando menús profundos y complejos.  

Legibilidad bajo el Sol	

Se empleará una paleta de colores de alto contraste (texto oscuro sobre fondos claros) y fuentes grandes y legibles (sans-serif) para garantizar la visibilidad bajo la luz solar directa.  

Navegación Simplificada	

La arquitectura de la información será lineal y basada en tareas. Se evitará la jerarquía de información compleja.  Los iconos siempre irán acompañados de etiquetas de texto claras y concisas.  

Formularios Optimizados	

Los formularios se dividirán en pasos lógicos ("chunking") para no abrumar al usuario.  Se utilizarán campos de entrada específicos (numéricos, fecha, selección única) para minimizar la necesidad de teclear. La lógica condicional ocultará campos irrelevantes para simplificar el formulario.  

Soporte Multilingüe	

La aplicación se lanzará con soporte para Español. Se planificará la futura inclusión de idiomas mayas prevalentes en las regiones cafetaleras, como Mam, Q'eqchi', K'iche' y Kaqchikel.  El diseño debe ser flexible para acomodar la longitud variable de las etiquetas en diferentes idiomas.  

Mockups de Pantallas (Concepto)

Pantalla 1: Inicio de Sesión y Menú Principal

    Diseño simple con campos grandes para usuario/contraseña o inicio de sesión con PIN.

    Menú principal con 4-5 botones grandes e iconografía clara: "Nueva Actividad", "Mis Tareas", "Asistencia", "Consultar Precios".

+----------------------------------------+

| AgroFinca Conectada |
| |
| |
| |
| |
| |
| |
| |
| |
| Usuario: Juan Pérez | Sinc: OK ✓ |
+----------------------------------------+

Pantalla 2: Formulario de Actividad (Paso 1)

    Formulario de una sola columna.   

    Uso de selectores y botones en lugar de texto libre siempre que sea posible.

+----------------------------------------+

| < Volver     NUEVA ACTIVIDAD     1/3 |
|----------------------------------------|
| Parcela: |
| |
| |
| Actividad: |
| |
| |
| Fecha: |
| [ Campo: 28 de julio, 2025       🗓️ ] |
| |
| |
| |
+----------------------------------------+

3. Integración con ERPNext

La integración se realizará a través de la REST API nativa del Frappe Framework, garantizando una comunicación segura y eficiente.  

Característica	Especificación Técnica
REST API Endpoints	

Se utilizarán los endpoints estándar /api/resource/:doctype para operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en los DocTypes relevantes (Ej: Tareas, Partes de horas, Empleados).  Se crearán métodos remotos (  

	/api/method/...) para lógica de negocio personalizada, como el cálculo de jornales.
Autenticación Segura	

La autenticación inicial se realizará mediante usuario y contraseña. La app solicitará un access_token a través de OAuth2 para las sesiones posteriores.  Como capa adicional de seguridad, se implementará la Autenticación de Dos Factores (2FA) de ERPNext, compatible con apps como Google Authenticator.  

Sincronización de Maestros	

Al iniciar sesión o periódicamente, la app descargará y almacenará localmente los datos maestros desde ERPNext (ej. lista de trabajadores, parcelas, tipos de actividad). Esto se logrará con una solicitud GET a /api/resource/:doctype con los filtros y campos necesarios.  

Upload de Archivos/Fotos	

Las fotos se subirán a través del endpoint /api/method/upload_file.  La solicitud será de tipo  
	

	

POST con multipart/form-data. Una vez subido, el file_url devuelto se adjuntará al DocType correspondiente (ej. en un campo "Adjunto" del registro de actividad).  

Notificaciones en Tiempo Real	Se configurarán webhooks en ERPNext para que, ante eventos específicos (ej. creación de una nueva tarea), se envíe una notificación a un servidor intermedio que, a su vez, activará una notificación push hacia el dispositivo del usuario.

4. Características Específicas para Caficultura

Característica	Descripción Funcional
Calculadoras de Campo	Cálculo de Jornal: Un módulo simple donde el supervisor ingresa la cantidad de quintales cosechados por un trabajador, y la app calcula el pago del día basado en la tarifa preconfigurada en ERPNext. Estimador de Producción: Permite registrar datos de muestreo (ej. número de frutos por bandola) para proyectar la producción estimada de una parcela.
Mapas de Parcelas con GPS	

Visualización de las parcelas de la finca en un mapa interactivo. El usuario podrá ver su ubicación actual vía GPS en relación con los límites de las parcelas.  Permitirá seleccionar una parcela directamente desde el mapa para iniciar un registro de actividad.  

Lista de Trabajadores y Asistencia	Los supervisores tendrán acceso a la lista de trabajadores asignados a su equipo. Podrán marcar la asistencia diaria (presente/ausente) con un solo toque. Esta información se sincronizará con el módulo de RRHH de ERPNext.
Códigos QR para Identificación	Se podrán generar códigos QR en ERPNext para identificar parcelas, equipos o sacos de café. La app tendrá un escáner QR integrado para identificar rápidamente el activo y precargar la información en un nuevo registro de actividad.
Consulta de Precios en Tiempo Real	

Un dashboard simple que mostrará el precio actualizado del café. Se integrará con una API de precios de commodities para obtener el precio del Contrato "C" de la bolsa de valores (ICE).  

5. Deployment y Distribución

Etapa	Plan de Acción
Publicación en Tiendas	

Se crearán cuentas de desarrollador en Google Play Store (pago único de $25) y Apple App Store (pago anual de $99).  Se prepararán todos los materiales necesarios para la tienda: íconos, capturas de pantalla, descripciones y políticas de privacidad.  

Sistema de Actualizaciones	Las actualizaciones se publicarán a través de los canales de las tiendas. La app verificará periódicamente si hay una nueva versión y notificará al usuario para que la instale, asegurando que todos utilicen la versión más reciente y segura.
Analytics y Crash Reporting	

Se integrará Firebase Crashlytics para el monitoreo en tiempo real de errores y fallos de la aplicación.  Esto permitirá identificar y solucionar problemas de manera proactiva, especialmente aquellos que puedan surgir en dispositivos de gama baja.  

Plan de Testing	

Pruebas Unitarias y de Integración: Se realizarán durante el desarrollo para asegurar la calidad del código. Pruebas Funcionales: Se validará que todas las características funcionen según lo especificado. Pruebas en Dispositivos Diversos: Se creará un laboratorio de pruebas con una selección de dispositivos que reflejen el mercado guatemalteco, incluyendo dispositivos de gama baja (ej. modelos antiguos de Samsung, Xiaomi, Motorola) para evaluar el rendimiento, consumo de batería y uso de memoria.  

	Pruebas de Campo (Beta): Un grupo selecto de trabajadores y supervisores reales utilizará la app en sus fincas para proporcionar retroalimentación sobre la usabilidad y funcionalidad en un entorno real.
Soporte Técnico	Se establecerá un canal de soporte a través de WhatsApp y un correo electrónico de contacto, gestionado por un equipo capacitado para resolver dudas y problemas de los usuarios. La información de contacto estará claramente visible en la sección "Ayuda" de la aplicación.