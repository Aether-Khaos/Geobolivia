from django.shortcuts import render
from django.http import JsonResponse
from .models import IndicadorClimatico

def dashboard(request):
    return render(request, 'dashboard.html')

def api_indicadores(request):
    categoria = request.GET.get('categoria', 'agropecuario')
    datos = IndicadorClimatico.objects.filter(categoria=categoria)
    
    resultado = {}
    for d in datos:
        if d.indicador not in resultado:
            resultado[d.indicador] = []
        resultado[d.indicador].append({
            'municipio': d.municipio,
            'valor': d.valor
        })
    
    return JsonResponse(resultado)

def buscar_municipio(request):
    texto = request.GET.get('q', '')

    resultados = IndicadorClimatico.objects.filter(
        municipio__icontains=texto
    ).values('municipio').distinct()

    data = list(resultados)
    return JsonResponse(data, safe=False)