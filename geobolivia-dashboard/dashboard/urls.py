from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('api/indicadores/', views.api_indicadores, name='api_indicadores'),
    path('buscar/', views.buscar_municipio, name='buscar_municipio'),
    path('subir-datos/', views.subir_datos, name='subir_datos'),
    path('descargar-datos/', views.descargar_datos, name='descargar_datos'),
    path('api/eventos-nasa/', views.api_eventos_nasa, name='api_eventos_nasa'),
    path('api/satelite-nasa/', views.api_satelite_nasa, name='api_satelite_nasa'),
        # Agrega estas líneas a urlpatterns
    path('api/metadatos/', views.api_metadatos, name='api_metadatos'),
    path('api/carga-logs/', views.api_carga_logs, name='api_carga_logs'),
    path('api/staging-validate/', views.api_staging_validate, name='api_staging_validate'),
    path('api/staging-publish/<int:staging_id>/', views.api_staging_publish, name='api_staging_publish'),
]