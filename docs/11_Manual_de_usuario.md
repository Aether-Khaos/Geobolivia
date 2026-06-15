# MANUAL DE USUARIO

## GeoBolivia Dashboard - Sistema de Monitoreo Climático

**Versión:** 1.0
**Fecha:** Junio de 2026

---

# 1. INTRODUCCIÓN

GeoBolivia Dashboard es un sistema web diseñado para la visualización de información climática y geográfica de Bolivia. El sistema integra mapas interactivos, gráficos estadísticos y eventos naturales detectados mediante información satelital de la NASA.

El sistema dispone de dos modalidades de acceso:

## Modo Visitante

* Permite visualizar el mapa interactivo, los gráficos estadísticos y los eventos de la NASA.
* No requiere registro ni autenticación.

## Modo Usuario Registrado

* Permite subir nuevos datos climáticos.
* Permite descargar información en formato CSV.
* Requiere la creación de una cuenta e inicio de sesión.

---

# 2. CÓMO ACCEDER AL SISTEMA

1. Abra un navegador web compatible (Google Chrome, Mozilla Firefox o Microsoft Edge).
2. Ingrese la siguiente dirección en la barra de direcciones:

```text
http://127.0.0.1:8000
```

3. Presione la tecla **Enter**.

La pantalla principal del sistema se cargará automáticamente.

---

# 3. PANTALLA PRINCIPAL

Al ingresar al sistema se presentan tres áreas principales:

| Área             | Ubicación                            | Función                                                                                  |
| ---------------- | ------------------------------------ | ---------------------------------------------------------------------------------------- |
| Mapa             | Lado izquierdo de la pantalla (75 %) | Muestra el territorio boliviano con sus departamentos, capitales, ríos, lagos y bosques. |
| Panel de Control | Lado derecho de la pantalla (24 %)   | Contiene botones, listas de información y opciones de configuración.                     |
| Menú de Usuario  | Esquina superior derecha             | Permite registrarse, iniciar sesión, subir datos y descargar información.                |

---

# 4. CÓMO USAR EL MAPA

## 4.1 Navegación dentro del mapa

| Acción                         | Procedimiento                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Acercar (Zoom In)              | Gire la rueda del mouse hacia adelante.                                       |
| Alejar (Zoom Out)              | Gire la rueda del mouse hacia atrás.                                          |
| Mover el mapa                  | Mantenga presionado el botón izquierdo del mouse y arrastre el cursor.        |
| Ver información de un elemento | Haga clic sobre cualquier departamento, capital o evento mostrado en el mapa. |

## 4.2 Capas del mapa

| Capa                     | Descripción                                                   |
| ------------------------ | ------------------------------------------------------------- |
| Departamentos            | Muestra los límites de los nueve departamentos de Bolivia.    |
| Capitales                | Muestra las capitales departamentales.                        |
| Lagos                    | Muestra los principales cuerpos de agua.                      |
| Ríos                     | Muestra la red hidrográfica.                                  |
| Bosques                  | Muestra las áreas forestales.                                 |
| Agropecuario             | Muestra las zonas agrícolas y ganaderas.                      |
| Eventos Naturales (NASA) | Muestra los eventos naturales activos detectados por la NASA. |

**Para activar una capa:** haga clic en la casilla correspondiente.

**Para desactivar una capa:** vuelva a hacer clic sobre la misma casilla.

---

# 5. EVENTOS NATURALES DE LA NASA

El sistema consulta periódicamente los servicios de la NASA para mostrar eventos naturales activos registrados en territorio boliviano.

## 5.1 Tipos de eventos

| Evento                  | Color de Referencia |
| ----------------------- | ------------------- |
| Incendio Forestal       | Naranja             |
| Inundación              | Azul                |
| Tormenta                | Amarillo            |
| Actividad Volcánica     | Rojo                |
| Sequía                  | Ámbar               |
| Deslizamiento de Tierra | Café                |

## 5.2 Visualización de eventos

### Desde el mapa

1. Active la capa **Eventos Naturales (NASA)**.
2. Identifique los eventos representados en el mapa.
3. Haga clic sobre cualquier evento para visualizar sus detalles.

### Desde el panel derecho

1. Desplácese hacia la sección **Eventos activos detectados por la NASA**.
2. Seleccione cualquier evento de la lista.
3. El mapa se desplazará automáticamente hasta la ubicación seleccionada.

---

# 6. GRÁFICOS ESTADÍSTICOS

El sistema presenta gráficos de barras organizados en tres categorías principales.

## Categorías disponibles

### Agropecuario

* Precipitación.
* Temperatura.
* Rendimiento de cultivos.

### Agua

* Caudal de ríos.
* Calidad del agua.

### Bosques

* Deforestación.
* Áreas protegidas.

## Actualización del gráfico

1. Seleccione una categoría.
2. Presione **Actualizar Gráfico**.
3. El sistema generará automáticamente el gráfico correspondiente.

## Indicadores estadísticos

* **Promedio:** Valor medio de los indicadores.
* **Máximo:** Valor más alto registrado.
* **Mínimo:** Valor más bajo registrado.
* **Total:** Número de indicadores disponibles.

---

# 7. METADATOS DE CAPAS

La sección **Metadatos de Capas** presenta información técnica de cada capa del sistema.

Para visualizar los detalles:

1. Ubique la capa de interés.
2. Seleccione la capa.
3. Revise la información disponible:

   * Descripción.
   * Fuente de datos.
   * Fecha de publicación.
   * Responsable.

---

# 8. REGISTRO DE NUEVO USUARIO

1. Abra el menú principal.
2. Seleccione **Registrarse**.
3. Complete el formulario:

| Campo              | Obligatorio | Ejemplo            |
| ------------------ | ----------- | ------------------ |
| Usuario            | Sí          | `juan_perez`       |
| Correo electrónico | No          | `juan@ejemplo.com` |
| Contraseña         | Sí          | `******`           |

4. Presione **Registrarse**.
5. El sistema iniciará sesión automáticamente.

---

# 9. INICIAR SESIÓN

1. Abra el menú principal.
2. Seleccione **Iniciar Sesión**.
3. Ingrese su usuario y contraseña.
4. Presione **Ingresar**.

---

# 10. SUBIR DATOS

> Disponible únicamente para usuarios registrados.

| Campo     | Ejemplo             |
| --------- | ------------------- |
| Categoría | Agropecuario        |
| Indicador | Precipitación anual |
| Municipio | La Paz              |
| Valor     | 850.5               |

Después de completar el formulario, presione **Subir Datos**.

El sistema mostrará el mensaje:

```text
Datos subidos correctamente.
```

---

# 11. DESCARGAR DATOS

> Disponible únicamente para usuarios registrados.

El sistema descargará automáticamente el archivo:

```text
indicadores_climaticos.csv
```

Ejemplo de contenido:

```csv
Categoria,Indicador,Municipio,Valor
agropecuario,Precipitación,La Paz,850.5
agropecuario,Temperatura,Cochabamba,18.3
```

---

# 12. CERRAR SESIÓN

1. Abra el menú principal.
2. Seleccione **Cerrar Sesión**.
3. El sistema finalizará la sesión y volverá al modo visitante.

---

# 13. SOLUCIÓN DE PROBLEMAS

| Problema                           | Posible causa                                   | Solución                                    |
| ---------------------------------- | ----------------------------------------------- | ------------------------------------------- |
| El mapa no se visualiza            | No existe conexión a Internet                   | Verifique su conexión de red.               |
| Los eventos de la NASA no aparecen | No existen eventos activos en Bolivia           | Espere nuevas actualizaciones.              |
| No puedo subir datos               | No ha iniciado sesión                           | Inicie sesión desde el menú principal.      |
| No puedo descargar datos           | No ha iniciado sesión                           | Inicie sesión desde el menú principal.      |
| El mapa funciona lentamente        | La capa de bosques requiere mayor procesamiento | Desactive temporalmente la capa de bosques. |
| El gráfico no se actualiza         | Error temporal                                  | Actualice la página con la tecla F5.        |
| Olvidé mi contraseña               | —                                               | Contacte al administrador del sistema.      |

---

# 14. PREGUNTAS FRECUENTES

## ¿Necesito pagar para utilizar el sistema?

No. El sistema es completamente gratuito.

## ¿Puedo visualizar el mapa sin registrarme?

Sí. La visualización pública no requiere registro.

## ¿Por qué debo registrarme para subir datos?

Porque únicamente los usuarios autorizados pueden incorporar información al sistema.

## ¿Cada cuánto se actualizan los eventos de la NASA?

La información se actualiza automáticamente de forma periódica.

## ¿Puedo utilizar el sistema desde un teléfono móvil?

Sí. La interfaz se adapta automáticamente a dispositivos móviles.

## ¿Qué debo hacer si encuentro un error?

Reporte el problema al administrador del sistema e incluya una captura de pantalla.

---

# 15. CONTACTO Y SOPORTE

**Correo electrónico:** `[correo institucional]`

**Tiempo de respuesta estimado:** 48 horas hábiles.
