from django.urls import path
from . import views

urlpatterns = [
    # Ruta principal del dashboard (ahora protegida)
    path('', views.dashboard, name='dashboard'),
    
    # Ruta para el sistema de inicio de sesión (Login)
    path('login/', views.login_view, name='login'),
    
    # Ruta para los datos de los indicadores
    path('api/indicadores/', views.api_indicadores, name='api_indicadores'),

    path('buscar/', views.buscar_municipio, name='buscar_municipio'),
]
