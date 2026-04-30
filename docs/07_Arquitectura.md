# 07. Arquitectura del Sistema

## Enfoque general
Sistema monolito modular: una sola aplicación dividida internamente por módulos (mapas, datos, gráficos, carga).

## Patrón arquitectónico
- **Hexagonal**: lógica de negocio separada de tecnología externa.
- **Capas**: Presentación → Lógica → Datos.

## Stack tecnológico
| Capa | Tecnología |
|------|-------------|
| Backend | Django + Django REST Framework |
| Base de datos | PostgreSQL + PostGIS |
| Frontend | React (SPA) |
| Mapas | Leaflet + GeoServer |
| Gráficos | Chart.js |
| Autenticación | Sesión + RBAC (roles) |

## Flujo de datos
1. Usuario → Frontend (React)
2. Frontend → API (Django REST)
3. API → Base de datos (PostgreSQL/PostGIS)
4. Resultado → Dashboard y mapas

## Seguridad
- Control de acceso por roles (RBAC)
- Contraseñas hasheadas (bcrypt)
- Separación de datos públicos / restringidos