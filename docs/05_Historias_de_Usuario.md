# 05. Historias de Usuario

## 5.1 Tabla de Trazabilidad (RF → HU)

| ID RF                      | ID HU | Relación                                    |
| -------------------------- | ----- | ------------------------------------------- |
| RF-04, RF-05, RF-09, RF-10 | HU-01 | Visualización de dashboard y mapa           |
| RF-06, RF-08               | HU-02 | Búsqueda geográfica                         |
| RF-07                      | HU-03 | Búsqueda por atributos                      |
| RF-11, RF-12               | HU-04 | Descarga de información con control por rol |
| RF-13, RF-14, RF-15, RF-19 | HU-05 | Carga y validación administrativa           |
| RF-20, RF-21               | HU-06 | Acceso público y restringido                |
| RF-16, RF-17               | HU-07 | Publicación interoperable y metadatos       |
| RF-18                      | HU-08 | Actualización incremental                   |
| RF-02, RF-03, RF-23, RF-24 | HU-09 | Uso analítico para decisiones               |
| RF-01, RF-13, RF-14        | HU-10 | Integración y limpieza de datos             |


## 5.2 Priorización del Product Backlog

* **Must:** Funcionalidades obligatorias
* **Should:** Funcionalidades importantes
* **Could:** Funcionalidades opcionales


## 5.3 Historias de Usuario

### HU-01 (Must)

**Como** técnico de GeoBolivia
**Quiero** visualizar dashboards con mapas e indicadores climáticos
**Para** interpretar rápidamente la información por categoría y territorio

**Criterios de aceptación:**

1. El dashboard debe mostrar mapa interactivo y gráficos asociados.
2. Debe actualizarse según filtros aplicados.
3. Debe estar disponible vía navegador web.


### HU-02 (Must)

**Como** usuario técnico
**Quiero** buscar un municipio o comunidad por nombre
**Para** centrar el mapa rápidamente en la zona de interés

**Criterios de aceptación:**

1. El sistema debe incluir un buscador geográfico.
2. Al seleccionar un resultado, el mapa debe centrarse automáticamente.
3. La búsqueda debe funcionar con nombres válidos cargados en el sistema.


### HU-03 (Should)

**Como** analista institucional
**Quiero** filtrar información por atributos o palabras clave
**Para** identificar zonas o registros con condiciones específicas

**Criterios de aceptación:**

1. El sistema debe aceptar búsqueda por palabra clave.
2. El resultado debe reflejarse en mapa y gráficos.
3. Debe limitarse a información existente en la base validada.


### HU-04 (Must)

**Como** usuario autorizado
**Quiero** descargar información visualizada en formatos abiertos
**Para** reutilizarla en análisis técnicos propios

**Criterios de aceptación:**

1. El sistema debe permitir descargar CSV para datos tabulares.
2. El sistema debe permitir descargar GeoJSON o shapefile para datos geográficos según disponibilidad.
3. Si la información es restringida, el sistema debe verificar el rol del usuario antes de habilitar la descarga.


### HU-05 (Must)

**Como** administrador de GeoBolivia
**Quiero** subir archivos nuevos desde una interfaz administrativa
**Para** actualizar la información sin depender de consola ni de un desarrollador

**Criterios de aceptación:**

1. El módulo debe permitir subir archivos compatibles definidos por la institución.
2. El sistema debe validar el archivo antes de insertarlo.
3. Si hay errores, debe mostrar mensajes claros y no cargar el archivo a producción.


### HU-06 (Must)

**Como** usuario público o autorizado
**Quiero** acceder solo a la información que corresponde a mi nivel de acceso
**Para** proteger datos sensibles sin impedir la consulta pública

**Criterios de aceptación:**

1. Los dashboards públicos deben abrir sin autenticación.
2. La información restringida debe requerir autenticación.
3. Las descargas sensibles deben estar condicionadas por rol.


### HU-07 (Must)

**Como** responsable técnico
**Quiero** publicar datos y metadatos compatibles con GeoBolivia e IDE-EPB
**Para** garantizar interoperabilidad institucional

**Criterios de aceptación:**

1. Cada capa debe conservar metadatos básicos.
2. La estructura publicada debe poder validarse técnicamente.
3. La solución debe respetar la normativa técnica institucional.


### HU-08 (Must)

**Como** administrador
**Quiero** que nuevas cargas actualicen la información del sistema de forma incremental
**Para** mantener vigente el tablero después de la consultoría

**Criterios de aceptación:**

1. El sistema debe aceptar nuevas cargas posteriores a la primera implementación.
2. Los datos aprobados deben reflejarse en el dashboard.
3. El proceso no debe requerir intervención del desarrollador.


### HU-09 (Must)

**Como** responsable institucional
**Quiero** consultar información climática organizada y útil
**Para** apoyar decisiones y análisis de cambio climático

**Criterios de aceptación:**

1. El sistema debe mostrar datos estructurados por sector.
2. Debe permitir análisis territorial básico.
3. Debe facilitar interpretación mediante indicadores visibles.


### HU-10 (Must)

**Como** administrador técnico
**Quiero** que el sistema valide integridad y estructura antes de insertar información
**Para** evitar datos corruptos en la base principal

**Criterios de aceptación:**

1. La carga debe pasar por validación previa.
2. Deben revisarse estructura, geometrías y duplicados.
3. Solo las cargas exitosas pasan a producción.