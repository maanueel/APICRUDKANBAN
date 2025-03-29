Parte 1: Ejecutar el Archivo Ejecutable (.exe)
Navegar a la Carpeta del Ejecutable:

Abre el "Símbolo del sistema" o "Windows PowerShell".
Usa el comando cd para ir a la carpeta dist donde está el ejecutable.
Ejecutar el Archivo:

Ejecuta el archivo ejecutable.
Verifica que el servidor esté corriendo (deberías ver un mensaje indicando que está en http://127.0.0.1:8001).
Parte 2: Usar la Colección de Postman
Abrir Postman:

Inicia la aplicación Postman.
Importar la Colección:

Haz clic en "Import" y selecciona el archivo JSON de la colección.
Haz clic en "Import" para agregarla.
Ejecutar Solicitudes:

Selecciona una solicitud de la colección (por ejemplo, "Obtener todas las tareas").
Asegúrate de que el método y la URL sean correctos (http://localhost:8001/tasks/).
Enviar la Solicitud:

Haz clic en "Send" y verifica la respuesta en la parte inferior.
Repetir para Otras Solicitudes:

Repite el proceso para otras solicitudes (Crear, Actualizar, Eliminar tareas).
