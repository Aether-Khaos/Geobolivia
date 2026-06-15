from django.contrib import admin
from .models import IndicadorClimatico, MetadatoCapa, CargaLog, StagingData

@admin.register(IndicadorClimatico)
class IndicadorClimaticoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'indicador', 'municipio', 'valor')
    list_filter = ('categoria', 'indicador')
    search_fields = ('municipio', 'indicador')

@admin.register(MetadatoCapa)
class MetadatoCapaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fuente', 'fecha_publicacion', 'fecha_actualizacion')
    list_filter = ('fuente', 'nombre_capa')
    search_fields = ('titulo', 'descripcion')

@admin.register(CargaLog)
class CargaLogAdmin(admin.ModelAdmin):
    list_display = ('archivo_nombre', 'usuario', 'estado', 'fecha_subida')
    list_filter = ('estado', 'categoria')
    search_fields = ('archivo_nombre', 'usuario')

@admin.register(StagingData)
class StagingDataAdmin(admin.ModelAdmin):
    list_display = ('archivo_nombre', 'usuario', 'estado_validacion', 'fecha_subida')
    list_filter = ('estado_validacion', 'categoria')