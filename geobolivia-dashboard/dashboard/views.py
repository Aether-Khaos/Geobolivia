from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import IndicadorClimatico

# 1. VISTA DEL DASHBOARD (Restringida)
@login_required
def dashboard(request):
    # Ahora 'acceso_publico' es False porque requiere estar logueado
    return render(request, 'dashboard.html', {
        'acceso_publico': False
    })

# 2. VISTA DE LOGIN (Nueva para tu tarea)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
            
    return render(request, 'login.html')

# 3. API DE INDICADORES (Lo que ya existía)
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