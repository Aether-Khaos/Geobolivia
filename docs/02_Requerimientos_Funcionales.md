# 2. Requerimientos Funcionales

Los requerimientos funcionales fueron definidos del TDR del proyecto. Se priorizo  las funcionalidades propias del sistema, excluyendo actividades de consultoría o análisis.

| ID | Descripción del requerimiento | Prioridad (MoSCoW) | Criterio de aceptación |
|---|---|---|---|
| RF-01 | El sistema debe permitir importar información geográfica de cambio climático en formatos geoespaciales validados. | Must | El sistema acepta al menos shapefile y GeoJSON y los incorpora al flujo de procesamiento. |
| RF-02 | El sistema debe permitir importar información estadística asociada a variables climáticas desde archivos tabulares validados. | Must | El sistema acepta al menos CSV y Excel con estructura compatible y asocia los datos a entidades geográficas. |
| RF-03 | El sistema debe organizar la información en categorías temáticas del sector agropecuario, agua y bosques. | Must | El usuario puede visualizar y consultar la información separada por las categorías definidas. |
| RF-04 | El sistema debe publicar la información procesada mediante tableros de control accesibles en entorno web. | Must | El dashboard se abre desde navegador y muestra datos activos del sistema. |
| RF-05 | El sistema debe mostrar datos dinámicos actualizados a partir de la base de datos geográfica. | Must | Un cambio validado en la base se refleja en el dashboard sin recarga manual prolongada. |
| RF-06 | El sistema debe permitir filtrar la información por municipio, cuenca u otra unidad territorial relevante. | Must | El usuario aplica un filtro geográfico y el mapa y los gráficos se actualizan con los resultados correspondientes. |
| RF-07 | El sistema debe permitir filtrar información por atributos temáticos o palabras clave. | Should | El usuario ingresa una palabra clave y el sistema devuelve solo la información relacionada. |
| RF-08 | El sistema debe incluir un buscador geográfico por nombre de municipio o comunidad. | Must | Al escribir una ubicación válida, el sistema centra el mapa en la zona seleccionada. |
| RF-09 | El sistema debe integrar mapas interactivos para visualizar capas georreferenciadas. | Must | El visor permite al menos zoom, desplazamiento, selección de capas y visualización de información emergente. |
| RF-10 | El sistema debe mostrar gráficos e indicadores climáticos vinculados a la selección geográfica o temática del usuario. | Must | Al cambiar filtros o ubicación, los gráficos se actualizan de forma coherente con el mapa. |
| RF-11 | El sistema debe permitir descargar información visualizada en formatos abiertos. | Must | El sistema permite descargar datos tabulares en CSV y datos geográficos en GeoJSON o shapefile, según permisos. |
| RF-12 | El sistema debe diferenciar la descarga de información pública y restringida según rol del usuario. | Must | El botón responde según permisos del usuario. |
| RF-13 | El sistema debe permitir la carga incremental de nuevos datos mediante un módulo administrativo. | Must | Un administrador puede subir archivos sin intervención técnica. |
| RF-14 | El sistema debe validar los archivos cargados antes de insertarlos en la base principal. | Must | Si hay errores, el sistema rechaza la carga y muestra detalles. |
| RF-15 | El sistema debe usar un área temporal de carga (staging) antes de publicar datos. | Should | Los datos solo pasan a producción tras validación exitosa. |
| RF-16 | El sistema debe registrar metadatos por cada conjunto de datos procesado. | Must | Cada capa contiene fuente, fecha y descripción. |
| RF-17 | El sistema debe cumplir con la normativa técnica GeoBolivia e IDE-EPB. | Must | Los datos cumplen estándares de interoperabilidad. |
| RF-18 | El sistema debe permitir la actualización incremental de información. | Must | Nuevas cargas se reflejan en el dashboard. |
| RF-19 | El sistema debe incluir un módulo administrativo para gestionar cargas. | Should | El administrador visualiza estados de carga. |
| RF-20 | El sistema debe permitir acceso público a dashboards no sensibles. | Must | Un usuario sin login puede visualizar datos públicos. |
| RF-21 | El sistema debe restringir información sensible por roles. | Must | Datos restringidos no se muestran sin autenticación. |
| RF-22 | El sistema debe permitir consultas espaciales eficientes. | Should | El sistema responde sin bloquear la interfaz. |
| RF-23 | El sistema debe apoyar la toma de decisiones climáticas. | Must | El dashboard muestra indicadores relevantes. |
| RF-24 | El sistema debe permitir identificar zonas vulnerables o pequeños productores. | Could | Se pueden aplicar filtros específicos cuando los datos lo permitan. |
