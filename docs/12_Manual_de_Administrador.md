# MANUAL DE ADMINISTRADOR

## GeoBolivia Dashboard - Sistema de Monitoreo Climático

**Versión:** 1.0
**Audiencia:** Personal de soporte TI y administradores de sistemas
**Perfil requerido:** Conocimientos básicos de línea de comandos Linux y navegación web.

---

# 1. PROPÓSITO DEL MANUAL

El presente documento está dirigido al personal técnico responsable de la instalación, configuración, operación y mantenimiento del sistema GeoBolivia Dashboard.

El manual proporciona procedimientos y lineamientos para:

* Instalar el sistema desde cero.
* Gestionar usuarios y permisos de acceso.
* Administrar los datos climáticos y sus metadatos.
* Monitorear la integración con la API de la NASA.
* Resolver problemas operativos frecuentes.
* Realizar procesos de respaldo y recuperación de información.

---

# 2. REQUISITOS DEL SISTEMA

## 2.1 Hardware mínimo recomendado

**Procesador**

* Mínimo de dos núcleos a 2.0 GHz.

**Memoria RAM**

* Mínimo de 4 GB.
* Recomendado: 8 GB.

**Almacenamiento**

* Al menos 2 GB de espacio libre.
* Espacio adicional para archivos GeoJSON.

**Conectividad de red**

* Conexión a Internet para la comunicación con la API de la NASA.

## 2.2 Software base requerido

**Sistema Operativo**

* Ubuntu 20.04 LTS o superior.
* Compatible con Debian y CentOS.

**Python**

* Versión 3.10 o superior.

Verificación:

```bash
python3 --version
```

**PIP**

* Versión 23.x o superior.

**SQLite**

* Versión 3.x.
* Incluido de manera predeterminada en Python.

## 2.3 Navegadores compatibles

* Google Chrome versión 120 o superior.
* Mozilla Firefox versión 115 o superior.
* Microsoft Edge versión 120 o superior.

---

# 3. INSTALACIÓN DEL SISTEMA

## 3.1 Obtención del código fuente

Si el proyecto se encuentra en un repositorio Git:

```bash
git clone [URL_DEL_REPOSITORIO] geobolivia-dashboard
cd geobolivia-dashboard
```

Si los archivos fueron recibidos por otro medio:

```bash
cp -r /ruta/origen/geobolivia-dashboard /opt/
cd /opt/geobolivia-dashboard
```

## 3.2 Creación del entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

Al activarse el entorno virtual aparecerá:

```text
(venv)
```

al inicio de la línea de comandos.

## 3.3 Instalación de dependencias

Si existe el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

En caso contrario:

```bash
pip install django==6.0.3 requests
```

## 3.4 Configuración de la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

## 3.5 Creación del usuario administrador

```bash
python manage.py createsuperuser
```

Ejemplo:

```text
Username: admin
Email address: admin@ejemplo.com
Password: [contraseña segura]
Password (again): [repetir contraseña]
```

## 3.6 Carga de metadatos iniciales

Ingresar a la consola de Django:

```bash
python manage.py shell
```

Crear los metadatos correspondientes a las capas:

* Departamentos
* Capitales
* Bosques
* Ríos
* Lagos

Al finalizar deberá aparecer el mensaje:

```text
Metadatos creados correctamente.
```

## 3.7 Verificación de archivos GeoJSON

Los archivos cartográficos deben encontrarse en:

```text
dashboard/static/dashboard/geojson/
```

Verificar la existencia de:

* departamentos.geojson
* capitales.geojson
* lagos.geojson
* rios.geojson
* bosques.geojson
* agropecuario.geojson

Si alguno de los archivos no existe, deberá copiarse a la ubicación indicada.

## 3.8 Inicio del servidor

Para pruebas y desarrollo:

```bash
python manage.py runserver 0.0.0.0:8000
```

La configuración para producción se describe en la Sección 13.

## 3.9 Verificación de la instalación

Acceder desde un navegador:

```text
http://[IP_DEL_SERVIDOR]:8000
```

Verificar que:

* El mapa se visualice correctamente.
* Las capas puedan activarse y desactivarse.
* El menú principal funcione adecuadamente.
* La integración con la API de la NASA responda correctamente.

---

# 4. ESTRUCTURA DE DIRECTORIOS

```text
/opt/geobolivia-dashboard/
├── dashboard/
│   ├── static/dashboard/geojson/
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── registro.html
│   │   └── subir_datos.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── geobolivia_project/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

# 5. GESTIÓN DE USUARIOS

El sistema permite realizar las siguientes tareas administrativas:

* Consultar usuarios registrados.
* Cambiar contraseñas.
* Otorgar permisos de administrador.
* Eliminar usuarios existentes.
* Crear nuevos usuarios desde la línea de comandos.

Todas las operaciones se realizan mediante el shell de Django:

```bash
python manage.py shell
```

---

# 6. GESTIÓN DE DATOS CLIMÁTICOS

Las funciones administrativas disponibles incluyen:

* Consultar la cantidad total de registros.
* Visualizar registros por categoría.
* Eliminar datos de categorías específicas.
* Consultar los últimos registros incorporados al sistema.

Estas operaciones permiten mantener la consistencia y la calidad de la información climática almacenada.

---

# 7. GESTIÓN DE METADATOS

El sistema permite:

* Consultar todos los metadatos existentes.
* Modificar la descripción de una capa.
* Incorporar nuevas capas geográficas y sus metadatos asociados.

Los metadatos constituyen la documentación técnica de las capas geoespaciales y facilitan la trazabilidad y administración de la información.

---

# 8. INTEGRACIÓN CON LA API DE LA NASA

El sistema se integra con la API EONET (Earth Observatory Natural Event Tracker) de la NASA.

Características principales:

* Consulta automática de eventos naturales activos.
* Almacenamiento temporal mediante caché.
* Tiempo de vida de la caché de una hora.
* Protección ante límites de solicitudes de la API.

El administrador puede:

* Probar la conectividad con la NASA.
* Limpiar manualmente la caché.
* Verificar el estado de los eventos almacenados.

---

# 9. RESPALDOS Y RECUPERACIÓN

Se recomienda implementar una política de respaldos periódicos.

El sistema permite:

* Respaldar completamente la base de datos SQLite.
* Exportar indicadores climáticos en formato JSON.
* Generar copias de seguridad de los archivos GeoJSON.
* Restaurar respaldos completos o parciales.
* Automatizar el proceso mediante tareas programadas utilizando `cron`.

---

# 10. MONITOREO Y REGISTROS DEL SISTEMA

Las actividades de monitoreo recomendadas incluyen:

* Supervisión de registros del servidor.
* Verificación de procesos activos.
* Comprobación del estado del puerto de escucha.
* Monitoreo del consumo de memoria RAM.
* Monitoreo del espacio disponible en disco.

## Códigos HTTP de interés

* **200:** Solicitud exitosa.
* **304:** Recurso obtenido desde la caché.
* **404:** Recurso no encontrado.
* **500:** Error interno del servidor.

---

# 11. SOLUCIÓN DE PROBLEMAS

Problemas comunes:

* Puerto de servicio ocupado.
* Dependencias de Python faltantes.
* Fallos de conectividad con la API de la NASA.
* Archivos GeoJSON inexistentes o dañados.
* Errores de validación CSRF.
* Bloqueos de la base de datos SQLite.
* Lentitud en la carga de la capa de bosques.

Cada situación debe ser diagnosticada siguiendo los procedimientos descritos en este manual antes de proceder al escalamiento.

---

# 12. OPTIMIZACIÓN DEL ARCHIVO DE BOSQUES

El archivo `bosques.geojson` posee un tamaño aproximado de 413 MB y puede afectar significativamente el rendimiento del sistema.

Se recomienda:

* Verificar periódicamente su tamaño.
* Reducir la precisión de las coordenadas.
* Simplificar geometrías cuando sea posible.
* Generar versiones optimizadas para ambientes de producción.

Estas acciones reducen el tiempo de carga y el consumo de memoria del navegador.

---

# 13. DESPLIEGUE EN PRODUCCIÓN

Para ambientes productivos se recomienda utilizar:

**Servidor de aplicaciones**

* Gunicorn.

**Servidor web**

* Nginx configurado como proxy inverso.

Configuraciones mínimas:

* Desactivar el modo `DEBUG`.
* Configurar correctamente `ALLOWED_HOSTS`.
* Crear un servicio `systemd` para el inicio automático.
* Configurar Nginx para servir archivos estáticos y redireccionar las solicitudes al servicio Gunicorn.

---

# 14. ACTUALIZACIONES DEL SISTEMA

El procedimiento de actualización comprende:

1. Obtener la versión más reciente del código.
2. Actualizar las dependencias de Python.
3. Aplicar migraciones de la base de datos.
4. Reiniciar los servicios correspondientes.

Se recomienda realizar un respaldo completo antes de cualquier actualización.

---

# 15. CONTACTO Y ESCALAMIENTO

Para problemas que no puedan resolverse mediante los procedimientos establecidos en este documento, deberá realizarse el escalamiento correspondiente.

**Errores en el código fuente**

* Desarrollador responsable del sistema.

**Problemas relacionados con datos geoespaciales**

* GeoBolivia – IDE-EPB.

**Problemas relacionados con la API de eventos**

* NASA Earth Observatory.

**Problemas de infraestructura, servidores o redes**

* Área de Tecnologías de Información de la institución.

---
