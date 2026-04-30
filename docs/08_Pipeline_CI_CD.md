# 08. Pipeline CI/CD

## Herramienta sugerida
GitHub Actions o GitLab CI (por simplicidad)

## Entornos
- `development` (local del consultor)
- `staging` (validación con GeoBolivia)
- `production` (servidor final)

## Pasos del pipeline
1. **Test**: ejecutar pruebas unitarias de Django
2. **Build**: compilar frontend (React)
3. **Migraciones**: `python manage.py migrate`
4. **Despliegue** a staging
5. **Validación manual** (opcional)
6. **Despliegue a producción**

## Estrategia de despliegue
**Blue-Green**:
- Blue = producción actual
- Green = nueva versión
- Redirigir tráfico solo si Green funciona

## Prevención de errores
- Nunca desplegar sin ejecutar migraciones
- Pipeline debe fallar si hay migraciones pendientes