# 3. Requerimientos No Funcionales

Los requerimientos no funcionales incluye atributos de calidad, restricciones operativas del sistema y requisitos técnicos de entrega relacionados con mantenimiento, despliegue y sostenibilidad institucional.

| ID | Categoría | Descripción técnica | Métrica de éxito | Prioridad |
|---|---|---|---|---|
| RNF-01 | Usabilidad | La interfaz del sistema debe estar en español. | El 100% de textos visibles, mensajes y manuales entregados están en español. | Must |
| RNF-02 | Usabilidad | El sistema debe incluir manual de usuario y manual de administrador. | Se entregan ambos manuales con procedimientos de uso, administración y resolución básica de errores. | Must |
| RNF-03 | Usabilidad | El módulo administrativo debe ser comprensible para personal no programador. | Un técnico institucional puede ejecutar una carga guiada usando la interfaz y la plantilla definida. | Should |
| RNF-04 | Rendimiento | La carga inicial del dashboard debe mantenerse en un tiempo razonable. | El dashboard carga en menos de 5 segundos en condiciones normales de prueba. | Should |
| RNF-05 | Rendimiento | Los cambios aprobados en datos deben reflejarse con baja latencia en la visualización. | Los cambios validados se reflejan en el tablero en menos de 60 segundos. | Must |
| RNF-06 | Rendimiento | Las consultas espaciales y por atributos frecuentes deben responder sin degradación severa. | Las consultas comunes mantienen tiempos de respuesta operables para el usuario. | Should |
| RNF-07 | Seguridad | El sistema debe diferenciar acceso público y acceso restringido según rol. | Un usuario sin permisos no puede visualizar ni descargar información sensible. | Must |
| RNF-08 | Seguridad | La solución debe resguardar la confidencialidad de la información sensible tratada en la consultoría. | La arquitectura y operación evitan exposición de datos restringidos. | Must |
| RNF-09 | Integridad | La carga de datos debe validar estructura, geometrías, duplicados y consistencia antes de publicar información. | Las cargas inválidas son rechazadas con mensajes claros y no alteran la base principal. | Must |
| RNF-10 | Integridad | El sistema debe mantener trazabilidad básica de las cargas realizadas. | Cada carga registra fecha, estado, tipo de archivo y resultado de validación. | Should |
| RNF-11 | Control de acceso | El sistema debe implementar control de acceso para funciones administrativas. | Existe al menos un rol administrador y otro de consulta pública o restringida. | Must |
| RNF-12 | Mantenibilidad | El sistema debe entregarse con documentación técnica suficiente para mantenimiento institucional. | Se entrega documentación del sistema, componentes, dependencias y procedimientos básicos. | Must |
| RNF-13 | Mantenibilidad | Deben entregarse scripts de mantenimiento cuando formen parte de la solución. | Los scripts entregados son funcionales y están documentados. | Should |
| RNF-14 | Mantenibilidad | Debe entregarse una guía de instalación o despliegue reproducible. | Un técnico puede reinstalar o desplegar la solución siguiendo la guía entregada. | Must |
| RNF-15 | Compatibilidad | El sistema debe ser accesible desde navegadores web modernos. | Funciona correctamente en Chrome, Edge y Firefox recientes. | Must |
| RNF-16 | Compatibilidad | La interfaz debe adaptarse a diferentes tamaños de pantalla. | La solución es usable en escritorio, tablet y móvil. | Must |
| RNF-17 | Interoperabilidad | La publicación de datos y metadatos debe alinearse a la normativa de GeoBolivia e IDE-EPB. | La solución puede validarse técnicamente como compatible con el nodo GeoBolivia. | Must |
| RNF-18 | Entrega técnica | Todo el código, documentación y activos digitales producidos deben ser entregados a la institución. | Se entrega paquete completo con código fuente, manuales, configuraciones y artefactos definidos. | Must |

## Requerimientos DevOps

## 3.6 Requisitos DevOps, Operación y Entrega Técnica

| ID | Descripción técnica | Criterio de aceptación | Prioridad |
|---|---|---|---|
| RDEV-01 | El código fuente del sistema debe entregarse en un repositorio versionado y estructurado de forma clara para su transferencia institucional. | Se entrega repositorio con estructura clara, historial de cambios y acceso institucional al contenido final. | Must |
| RDEV-02 | La solución debe incluir una estructura técnica clara que permita identificar componentes principales, configuración y documentación del sistema. | El repositorio contiene organización coherente de carpetas y archivos técnicos de la solución final. | Must |
| RDEV-03 | La documentación técnica debe mantenerse alineada con la versión final del sistema entregado. | Los manuales, la guía técnica y la estructura documentada coinciden con el sistema realmente entregado. | Must |
| RDEV-04 | La solución debe incluir una guía de instalación o despliegue reproducible para permitir reinstalación institucional. | Un técnico puede reinstalar el sistema siguiendo la guía entregada sin depender del consultor original. | Must |
| RDEV-05 | Si la solución utiliza componentes como GeoServer, Django o base de datos geográfica, su configuración esencial debe quedar documentada. | La documentación administrativa incluye parámetros básicos de despliegue, dependencias y configuración mínima necesaria. | Must |
| RDEV-06 | Deben entregarse scripts o procedimientos documentados para tareas recurrentes de mantenimiento. | Se incluyen scripts o instrucciones para respaldo, actualización o limpieza, si forman parte de la solución final. | Should |
| RDEV-07 | El sistema debe registrar el resultado de las cargas de datos para facilitar seguimiento operativo. | Cada carga deja evidencia de fecha, estado, validación y resultado en el módulo administrativo o en el registro correspondiente. | Must |
| RDEV-08 | El proceso de carga de datos debe incorporar una etapa previa de validación antes de afectar la base principal. | Los archivos cargados pasan por una validación previa y solo se insertan a producción si cumplen las reglas definidas. | Must |
| RDEV-09 | El sistema debe mostrar mensajes de error legibles para el usuario durante la validación de cargas. | Ante errores de estructura o integridad, el sistema informa el problema sin exponer mensajes técnicos incomprensibles. | Must |
| RDEV-10 | La solución debe permitir actualización incremental de datos sin requerir intervención del desarrollador en cada carga. | El personal autorizado puede ejecutar nuevas cargas desde el módulo administrativo siguiendo el flujo definido. | Must |
| RDEV-11 | La solución debe conservar trazabilidad básica de las cargas de datos realizadas por usuarios autorizados. | El sistema conserva evidencia mínima de quién realizó una carga, cuándo la realizó y si fue aceptada o rechazada. | Should |
| RDEV-12 | La entrega técnica debe incluir los activos necesarios para operar la solución después de la consultoría. | Se entregan código fuente, configuraciones, manuales, guías, scripts y demás artefactos comprometidos en la solución final. | Must |
| RDEV-13 | La documentación debe facilitar la transferencia de conocimiento al equipo técnico institucional. | El manual de administrador y la guía técnica permiten a la institución comprender operación, configuración y mantenimiento básico. | Must |
| RDEV-14 | La solución debe contemplar separación entre información pública y restringida dentro del flujo operativo. | La operación del sistema distingue visualización pública y acceso restringido según reglas de autenticación y rol. | Must |
| RDEV-15 | La publicación de información debe ser consistente con la estructura interoperable requerida por GeoBolivia e IDE-EPB. | Los datos y metadatos entregados o publicados pueden ser revisados técnicamente según la normativa aplicable. | Must |
| RDEV-16 | La solución debe ser sostenible institucionalmente una vez concluida la consultoría. | El sistema puede seguir operándose con personal técnico institucional usando manuales, módulo administrativo y guía de instalación. | Must |
