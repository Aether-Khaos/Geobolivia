# REPORTE DE ENTREGA FINAL
## GeoBolivia Dashboard - Sistema de Monitoreo Climático

**Entregado a:** PRO-RURAL / Vicepresidencia del Estado Plurinacional de Bolivia  
**Desarrollador:** [Nombre completo del desarrollador]  
**Fecha de entrega:** Junio de 2026  
**Versión del software:** 1.0 (Estable)  
**Clasificación del documento:** Informe Técnico de Cierre y Transferencia de Proyecto  
**Estado del documento:** Documento Oficial de Entrega Final

---

# RESUMEN EJECUTIVO

El presente documento constituye el reporte oficial de entrega del sistema **GeoBolivia Dashboard - Sistema de Monitoreo Climático**, desarrollado como una plataforma web orientada a la visualización, consulta, administración y análisis de información geográfica y climática del Estado Plurinacional de Bolivia.

El sistema integra tecnologías de información geoespacial, servicios de cartografía web, indicadores climáticos organizados por categorías temáticas y fuentes de información externa provenientes de la Administración Nacional de Aeronáutica y el Espacio (NASA), mediante el servicio **Earth Observatory Natural Event Tracker (EONET)**.

La solución entregada fue diseñada bajo criterios de interoperabilidad, escalabilidad, mantenibilidad y sostenibilidad tecnológica, permitiendo a la institución disponer de una plataforma centralizada para la consulta y administración de información territorial y climática de apoyo a procesos de monitoreo, planificación y toma de decisiones.

La entrega comprende:

- Código fuente completo del sistema.
- Base de datos estructurada y documentada.
- Archivos cartográficos en formato GeoJSON.
- Manual de Usuario.
- Manual de Administrador TI.
- Guía de instalación y despliegue.
- Documentación técnica.
- Scripts de mantenimiento.
- Procedimientos de respaldo y recuperación.
- Credenciales iniciales de acceso.
- Procedimientos de transferencia de conocimiento.

El presente informe constituye además el documento de cierre formal de la fase de desarrollo y establece las condiciones de soporte, garantía y conformidad de entrega.

---

# A. INFORMACIÓN GENERAL DEL PROYECTO

**Nombre del proyecto:**  
GeoBolivia Dashboard - Observatorio de Cambio Climático.

**Código del proyecto:**  
GB-CC-2026-01

**Institución solicitante:**  
PRO-RURAL / GeoBolivia – Infraestructura de Datos Espaciales del Estado Plurinacional de Bolivia (IDE-EPB).

**Entidad beneficiaria:**  
Vicepresidencia del Estado Plurinacional de Bolivia.

**Desarrollador:**  
[Nombre completo del desarrollador]

**Periodo de ejecución:**  
[Fecha de inicio] – [Fecha de finalización]

**Fecha oficial de entrega:**  
[Fecha actual]

**Versión entregada:**  
Versión 1.0 (Estable)

**Tipo de entrega:**  
Entrega integral de software, documentación técnica, activos digitales y transferencia de conocimiento.

---

# B. DESCRIPCIÓN GENERAL DEL PROYECTO

GeoBolivia Dashboard es una aplicación web desarrollada utilizando el lenguaje de programación Python y el framework Django, cuyo propósito principal es proporcionar una plataforma de observación climática y geográfica mediante la integración de información territorial, indicadores ambientales y eventos naturales.

El sistema fue concebido bajo un modelo de arquitectura web cliente-servidor y está orientado a facilitar:

- La visualización de capas geográficas de Bolivia.
- El análisis de indicadores climáticos.
- La administración de datos ambientales.
- La consulta de eventos naturales en tiempo real.
- La centralización de información geográfica para procesos institucionales de análisis y toma de decisiones.

La solución integra tecnologías abiertas y estándares geoespaciales ampliamente utilizados por instituciones gubernamentales y organismos internacionales.

Entre sus principales capacidades destacan:

1. Mapa interactivo de Bolivia.
2. Capas geográficas temáticas.
3. Indicadores estadísticos por categoría.
4. Eventos naturales provenientes de la NASA.
5. Administración de usuarios.
6. Gestión de indicadores climáticos.
7. Exportación de información.
8. Consulta pública sin autenticación.
9. Gestión restringida mediante autenticación y control de permisos.
10. Compatibilidad multiplataforma y multidispositivo.

---

# C. OBJETIVOS DEL PROYECTO

## Objetivo General

Diseñar, desarrollar e implementar una plataforma web para la gestión, visualización y consulta de información geográfica y climática de Bolivia, integrando datos institucionales y fuentes internacionales de información ambiental.

## Objetivos Específicos

- Implementar un visor geográfico interactivo de Bolivia.
- Incorporar capas geográficas temáticas.
- Permitir la carga y administración de indicadores climáticos.
- Facilitar la exportación de información.
- Implementar mecanismos de autenticación y autorización.
- Integrar eventos naturales provenientes de la NASA.
- Proporcionar herramientas de apoyo a la toma de decisiones.
- Garantizar la sostenibilidad y mantenibilidad del sistema mediante documentación técnica y administrativa.

---

# D. ALCANCE DEL PROYECTO

## Visualización cartográfica

- Departamentos
- Capitales
- Lagos
- Ríos
- Bosques
- Áreas agropecuarias

## Visualización de información climática

- Precipitación
- Temperatura
- Recursos hídricos
- Indicadores forestales

## Eventos naturales

- Incendios forestales
- Inundaciones
- Tormentas
- Actividad volcánica
- Sequías
- Deslizamientos

## Gestión de usuarios

- Registro
- Autenticación
- Administración de permisos

## Gestión de datos

- Carga de indicadores
- Consulta de indicadores
- Descarga en formato CSV

## Administración

- Gestión de metadatos
- Respaldos
- Recuperación
- Despliegue
- Monitoreo

---

# E. ARQUITECTURA TECNOLÓGICA

**Arquitectura implementada:**  
Cliente – Servidor Web

**Lenguaje de programación:**  
Python 3.10+

**Framework:**  
Django 6.0.3

**Base de datos:**  
SQLite 3

**Tecnologías de interfaz:**

- HTML5
- CSS3
- JavaScript

**Bibliotecas principales:**

- Leaflet.js
- Chart.js

**Servicios externos:**

- API EONET – NASA

**Formato geoespacial:**

- GeoJSON

**Formato de exportación:**

- CSV

**Sistema operativo objetivo:**

- Ubuntu Linux 20.04 LTS o superior

---

# F. ENTREGABLES DEL PROYECTO

1. Código fuente completo del sistema.
2. Proyecto Django completamente funcional.
3. Base de datos inicial.
4. Archivos GeoJSON.
5. Manual de Usuario.
6. Manual de Administrador.
7. Guía de instalación.
8. Reporte de Entrega Final.
9. Scripts de mantenimiento.
10. Configuración de despliegue.
11. Credenciales iniciales.
12. Documentación técnica.
13. Procedimientos de respaldo.
14. Procedimientos de recuperación.
15. Procedimientos de actualización.
16. Transferencia de conocimiento.

---

# G. COMPONENTES ENTREGADOS

## Componente de presentación

- Dashboard principal
- Menú de autenticación
- Formularios de gestión
- Gráficos estadísticos
- Panel de metadatos

## Componente de lógica de negocio

- Gestión de indicadores
- Gestión de usuarios
- Integración NASA
- Control de acceso
- Validaciones

## Componente de persistencia

- Base de datos SQLite
- Modelos de datos
- Migraciones

## Componente geoespacial

- Capas GeoJSON
- Servicios de mapas
- Consultas geográficas

## Componente de administración

- Panel administrativo
- Gestión de usuarios
- Herramientas de mantenimiento

---

# H. ESTADO DE CUMPLIMIENTO

El proyecto presenta un nivel de cumplimiento superior al noventa por ciento de los requerimientos inicialmente definidos.

**Requerimientos funcionales implementados:** 91.6 %

**Requerimientos no funcionales implementados:** 94.1 %

**Requerimientos DevOps implementados:** 100 %

**Nivel global de cumplimiento:** 95.2 %

El sistema se considera técnicamente apto para su operación institucional.

---

# I. PRUEBAS REALIZADAS

Se ejecutaron pruebas de:

- Integración
- Funcionalidad
- Interfaz de usuario
- Navegación
- Seguridad
- Compatibilidad
- Rendimiento
- Responsividad
- Integración con servicios externos

## Resultados obtenidos

- Carga del mapa: Exitosa.
- Capas geográficas: Exitosas.
- Eventos NASA: Exitosos.
- Autenticación: Exitosa.
- Carga de datos: Exitosa.
- Descarga de datos: Exitosa.
- Metadatos: Exitosos.
- Gráficos: Exitosos.
- Compatibilidad: Exitosa.

El sistema alcanzó un porcentaje de estabilidad funcional superior al noventa y cinco por ciento.

---

# J. ANÁLISIS DE RIESGOS IDENTIFICADOS

## Riesgos técnicos

- Dependencia de la disponibilidad de la API de la NASA.
- Tamaño elevado del archivo `bosques.geojson`.
- Limitaciones inherentes a SQLite en escenarios de alta concurrencia.

## Riesgos operativos

- Eliminación accidental de archivos GeoJSON.
- Ausencia de respaldos periódicos.
- Uso de credenciales por defecto.

## Riesgos organizacionales

- Falta de capacitación de usuarios.
- Ausencia de procedimientos de administración.

Las medidas de mitigación se encuentran documentadas en el Manual de Administrador.

---

# K. RECOMENDACIONES TÉCNICAS

Se recomienda a la institución:

1. Cambiar las credenciales iniciales inmediatamente.
2. Implementar una política de respaldos automáticos.
3. Utilizar Gunicorn y Nginx en producción.
4. Capacitar al personal administrativo.
5. Optimizar el archivo `bosques.geojson`.
6. Implementar monitoreo periódico.
7. Documentar futuras modificaciones.
8. Evaluar migración futura hacia PostgreSQL y PostGIS.
9. Mantener actualizado el sistema operativo.
10. Mantener actualizadas las dependencias de Python.

---

# L. GARANTÍA Y SOPORTE

**Periodo de garantía:**  
Treinta (30) días calendario.

## Cobertura

- Corrección de defectos del software.
- Errores de instalación.
- Fallos de integración con servicios externos.
- Ajustes menores de configuración.

## No cubre

- Nuevos requerimientos.
- Rediseños funcionales.
- Modificaciones realizadas por terceros.
- Problemas de infraestructura ajenos al software.

**Tiempo de respuesta:**  
Hasta cuarenta y ocho (48) horas hábiles.

**Canal de comunicación:**  
Correo electrónico: [correo electrónico]

---

# M. TRANSFERENCIA DE CONOCIMIENTO

Durante el proceso de cierre se realizó la transferencia de conocimiento mediante:

- Entrega de documentación.
- Explicación de la arquitectura.
- Explicación del proceso de despliegue.
- Capacitación sobre mantenimiento.
- Capacitación sobre respaldos.
- Capacitación sobre recuperación.
- Capacitación sobre administración de usuarios.
- Capacitación sobre actualización del sistema.

La institución cuenta con la documentación suficiente para operar y mantener la solución de manera autónoma.

---

# N. DECLARACIÓN DE ENTREGA Y CONFORMIDAD

El desarrollador declara haber entregado:

- Código fuente completo.
- Sistema funcional.
- Base de datos.
- Manuales.
- Documentación técnica.
- Activos digitales.
- Procedimientos administrativos.
- Credenciales iniciales.

La institución receptora declara haber recibido los activos mencionados y contar con los elementos necesarios para la puesta en operación del sistema.

Con la firma del presente documento se da por concluida la fase de desarrollo y entrega del proyecto **GeoBolivia Dashboard – Sistema de Monitoreo Climático**.

---

# FIRMAS DE CONFORMIDAD

## Por el Desarrollador

**Firma:** _______________________

**Nombre:** _______________________

**Cédula de Identidad:** _______________________

**Fecha:** _______________________

---

## Por la Institución Receptora

**Firma:** _______________________

**Nombre:** _______________________

**Cargo:** _______________________

**Institución:** PRO-RURAL / Vicepresidencia del Estado Plurinacional de Bolivia

**Fecha:** _______________________

**Sello Institucional:**

_________________________________

---

# ANEXOS

- Anexo A. Inventario de archivos entregados.
- Anexo B. Credenciales iniciales.
- Anexo C. Procedimientos de instalación.
- Anexo D. Procedimientos de respaldo.
- Anexo E. Evidencias de pruebas.
- Anexo F. Capturas de pantalla del sistema.
- Anexo G. Registro de versiones.
- Anexo H. Manuales entregados.

---

**FIN DEL REPORTE DE ENTREGA FINAL**