from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/indicadores/', views.api_indicadores, name='api_indicadores'),
    path('buscar/', views.buscar_municipio),
]
