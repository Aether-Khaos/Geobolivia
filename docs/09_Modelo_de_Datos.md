# 09. Modelo de Datos (PostgreSQL + PostGIS)

## Tabla: `capa_geo`
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | serial | PK |
| nombre | varchar | Nombre de la capa |
| geometria | geometry(Polygon, 4326) | Geometría espacial |
| categoria | varchar | agropecuario / agua / bosques |
| fuente | varchar | Institución origen |
| fecha_carga | timestamp | |

## Tabla: `carga_log`
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | serial | PK |
| usuario_id | int | FK a usuario |
| archivo | varchar | Nombre del archivo |
| estado | varchar | éxito / error |
| mensaje_error | text | Si aplica |
| fecha | timestamp | |

## Tabla: `usuario`
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | serial | PK |
| username | varchar | Único |
| password_hash | varchar | bcrypt |
| rol | varchar | admin / publico |

## Tabla: `metadato`
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | serial | PK |
| capa_id | int | FK a capa_geo |
| descripcion | text | |
| fecha_publicacion | date | |
| norma_ide_epb | boolean | Cumple o no |