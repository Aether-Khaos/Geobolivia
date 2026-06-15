from django.db import models

class IndicadorClimatico(models.Model):
    categoria = models.CharField(max_length=100)
    indicador = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    valor = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.categoria} - {self.indicador} - {self.municipio}"

# NUEVO MODELO PARA METADATOS
class MetadatoCapa(models.Model):
    TIPO_CAPA = [
        ('departamentos', 'Departamentos'),
        ('capitales', 'Capitales'),
        ('lagos', 'Lagos'),
        ('rios', 'Ríos'),
        ('bosques', 'Bosques'),
        ('agropecuario', 'Agropecuario'),
        ('educativas', 'Unidades Educativas'),
        ('climatico', 'Datos Climáticos'),
    ]
    
    nombre_capa = models.CharField(max_length=100, choices=TIPO_CAPA)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fuente = models.CharField(max_length=200, default="GeoBolivia / NASA")
    fecha_publicacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    resolucion = models.CharField(max_length=50, blank=True, help_text="Ej: 250m, 500m, 1km")
    extension = models.CharField(max_length=20, default="GeoJSON")
    responsable = models.CharField(max_length=100, default="GeoBolivia")
    url_descarga = models.URLField(blank=True)
    url_metadatos = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha_publicacion}"

# NUEVO MODELO PARA TRAZABILIDAD DE CARGAS
class CargaLog(models.Model):
    ESTADO_CARGA = [
        ('pending', 'Pendiente'),
        ('validating', 'Validando'),
        ('approved', 'Aprobada'),
        ('rejected', 'Rechazada'),
        ('published', 'Publicada'),
    ]
    
    usuario = models.CharField(max_length=150)
    archivo_nombre = models.CharField(max_length=255)
    archivo_tipo = models.CharField(max_length=50)  # GeoJSON, CSV, Shapefile
    categoria = models.CharField(max_length=100, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    fecha_validacion = models.DateTimeField(null=True, blank=True)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CARGA, default='pending')
    validacion_mensaje = models.TextField(blank=True)
    registros_afectados = models.IntegerField(default=0)
    metadatos_id = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.archivo_nombre} - {self.estado} - {self.fecha_subida}"

# NUEVO MODELO PARA DATOS EN STAGING (ÁREA TEMPORAL)
class StagingData(models.Model):
    usuario = models.CharField(max_length=150)
    archivo_nombre = models.CharField(max_length=255)
    contenido_json = models.JSONField()  # Datos en bruto
    categoria = models.CharField(max_length=100)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    estado_validacion = models.CharField(max_length=50, default='pending')
    errores_validacion = models.TextField(blank=True)
    registros_validos = models.IntegerField(default=0)
    registros_invalidos = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Staging: {self.archivo_nombre} - {self.estado_validacion}"