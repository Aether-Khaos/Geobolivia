## Prototipo en Figma
[Ver prototipo]
(https://www.figma.com/make/jKc699XWoAcGN9aVfeQOAw/Herramienta-de-escritura?fullscreen=1&t=DayhJ0zsaAE6xQmR-1&preview-route=%2Fdashboard%2Fdatos)
Usuario:   (    alcozer@gmail.com      )         Contraseña:  (  alcocer123    )
# 6. Prototipo y Validación Visual

## 6.1 Flujo seleccionado
**Flujo completo de carga, validación y publicación de datos geoespaciales**

El flujo seleccionado para el prototipo corresponde al proceso mediante el cual un usuario administrador inicia sesión en el sistema, carga un archivo de datos, ejecuta la validación automática, recibe retroalimentación en caso de errores y, si la carga es aprobada, visualiza el impacto de los nuevos datos dentro del dashboard institucional.

Este flujo se considera prioritario porque representa una de las operaciones más importantes del sistema: mantener la información actualizada sin depender de procesos manuales externos ni de intervención constante del desarrollador.


## 6.2 Justificación del flujo

Se eligió este flujo porque concentra varias capacidades críticas del sistema dentro de una sola secuencia funcional completa. A través de este flujo se puede validar:

- La sostenibilidad del sistema después de la consultoría  
- La actualización incremental de la información  
- La facilidad de uso del módulo administrativo  
- La validación automática de datos antes de publicarlos  
- El manejo de errores comprensibles para el usuario  
- La relación entre la carga de datos y el dashboard final  
- El control de acceso mediante usuario administrador  

Además, este flujo está directamente respaldado por la entrevista y por el TDR, donde se menciona la necesidad de:

- Procesar y sistematizar información geográfica y estadística  
- Mostrar datos dinámicos actualizados  
- Permitir búsquedas, consultas y descargas  
- Entregar una solución utilizable y mantenible por la institución  
- Contar con manuales y documentación de apoyo  


## 6.3 Objetivo del prototipo

El objetivo del prototipo es representar visualmente cómo funcionará el proceso de actualización de información dentro del sistema, desde el ingreso del administrador hasta la publicación correcta de los datos en el dashboard.

No se busca prototipar todo el sistema, sino validar de manera clara y completa un solo flujo crítico que permita demostrar:

- Valor funcional  
- Secuencia lógica  
- Interacción del usuario  
- Puntos de control  
- Resultado final visible  


## 6.4 Alcance del prototipo

El prototipo abarcará únicamente el flujo administrativo de carga y actualización de datos.

### Incluye:
- Autenticación del administrador  
- Acceso al panel administrativo  
- Carga de archivo  
- Validación automática  
- Visualización de errores  
- Confirmación de carga exitosa  
- Visualización del dashboard actualizado  

### No incluye:
- Desarrollo del sistema real  
- Integración técnica real con base de datos  
- Configuración real de GeoServer  
- Implementación de todos los módulos del sistema  
- Prototipos de todos los flujos del proyecto  


## 6.5 Actores involucrados

### Administrador de GeoBolivia
Usuario principal del flujo, con permisos para ingresar al módulo administrativo, subir archivos y revisar resultados.

### Sistema de validación
Encargado de verificar la estructura del archivo, detectar errores y decidir si la carga es válida.

### Base de datos geográfica
Destino final de los datos aprobados.

### Dashboard institucional
Salida final del flujo donde se visualizan los datos actualizados.


## 6.6 Descripción general del flujo

1. El administrador inicia sesión en el sistema.  
2. El sistema valida sus credenciales.  
3. Accede al panel administrativo.  
4. Selecciona la opción de carga de datos.  
5. Escoge categoría y sube un archivo.  
6. El sistema valida automáticamente el archivo.  
7. Si hay errores, muestra mensajes claros.  
8. Si es válido, confirma la carga.  
9. El usuario visualiza los datos en el dashboard.  


## 6.7 Pantallas del prototipo

### 1. Inicio de sesión
- Usuario/correo  
- Contraseña  
- Botón de ingreso  
- Mensaje de acceso seguro  

### 2. Panel administrativo
- Menú (Dashboard, Cargar datos, Historial)  
- Indicador de usuario  
- Acceso a funciones  

### 3. Carga de datos
- Selector de categoría  
- Tipo de archivo  
- Subida de archivo  
- Botón “Validar y cargar”  

### 4. Pantalla de error
- Mensaje de error  
- Detalles del problema  
- Botón para reintentar  

### 5. Pantalla de éxito
- Confirmación de carga  
- Registros procesados  
- Fecha y categoría  
- Acceso al dashboard  

### 6. Dashboard
- Mapa interactivo  
- Gráficos  
- Filtros  
- Visualización de datos actualizados  


## 6.8 Comportamientos del flujo

El prototipo evidencia:

- Autenticación  
- Acceso administrativo  
- Carga de datos  
- Validación  
- Manejo de errores  
- Confirmación exitosa  
- Visualización final  


## 6.9 Historias de usuario

- HU-05: Carga de archivos  
- HU-06: Acceso por rol  
- HU-08: Actualización incremental  
- HU-10: Validación de datos  


## 6.10 Requerimientos funcionales

- RF-13: Carga incremental  
- RF-14: Validación de archivos  
- RF-15: Etapa de validación previa  
- RF-18: Actualización de información  
- RF-19: Módulo administrativo  
- RF-20 / RF-21: Control de acceso  
- RF-04 / RF-05: Dashboard actualizado  


## 6.11 Criterios de validación

El prototipo cumple si:

1. Presenta flujo completo  
2. Incluye error y éxito  
3. Identifica actores  
4. Es coherente con historias  
5. Cumple requerimientos  
6. Refleja impacto en dashboard  
7. Tiene coherencia visual  
8. Es usable y entendible  


## 6.12 Conclusión

El prototipo representa una secuencia completa del proceso de carga, validación y publicación de datos geoespaciales, permitiendo validar el funcionamiento del sistema y su utilidad para la institución.

Este flujo demuestra cómo el sistema puede mantener información actualizada de forma controlada, comprensible y sostenible, alineándose con los requerimientos definidos en el proyecto.
