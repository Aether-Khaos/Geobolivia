from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.cache import cache
from .models import IndicadorClimatico
import csv
import requests

def dashboard(request):
    return render(request, 'dashboard.html', {
        'user_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    })

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

def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'El usuario ya existe'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('dashboard')
    
    return render(request, 'registro.html')

def logout_view(request):
    logout(request)
    return redirect('dashboard')

def api_indicadores(request):
    categoria = request.GET.get('categoria', 'agropecuario')
    datos = IndicadorClimatico.objects.filter(categoria=categoria)
    
    resultado = {}
    for d in datos:
        if d.indicador not in resultado:
            resultado[d.indicador] = []
        resultado[d.indicador].append({
            'municipio': d.municipio,
            'valor': float(d.valor) if d.valor else 0
        })
    
    # Calcular promedios
    promedios = {}
    for indicador, valores in resultado.items():
        suma = sum(v['valor'] for v in valores)
        promedios[indicador] = suma / len(valores) if valores else 0
    
    return JsonResponse(promedios)

def buscar_municipio(request):
    texto = request.GET.get('q', '')
    
    if len(texto) < 2:
        return JsonResponse([], safe=False)
    
    resultados = IndicadorClimatico.objects.filter(
        municipio__icontains=texto
    ).values('municipio').distinct()[:10]
    
    return JsonResponse(list(resultados), safe=False)

@login_required
def subir_datos(request):
    if request.method == 'POST':
        try:
            categoria = request.POST.get('categoria')
            indicador = request.POST.get('indicador')
            municipio = request.POST.get('municipio')
            valor = request.POST.get('valor')
            
            nuevo_dato = IndicadorClimatico(
                categoria=categoria,
                indicador=indicador,
                municipio=municipio,
                valor=valor
            )
            nuevo_dato.save()
            messages.success(request, '✅ Datos subidos correctamente')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f'❌ Error: {str(e)}')
    
    categorias = IndicadorClimatico.objects.values_list('categoria', flat=True).distinct()
    indicadores = IndicadorClimatico.objects.values_list('indicador', flat=True).distinct()
    municipios = IndicadorClimatico.objects.values_list('municipio', flat=True).distinct()
    
    return render(request, 'subir_datos.html', {
        'categorias': categorias,
        'indicadores': indicadores,
        'municipios': municipios
    })

@login_required
def descargar_datos(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="indicadores.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Categoria', 'Indicador', 'Municipio', 'Valor'])
    
    for dato in IndicadorClimatico.objects.all():
        writer.writerow([dato.categoria, dato.indicador, dato.municipio, dato.valor])
    
    return response

def api_eventos_nasa(request):
    """Obtiene eventos naturales de la NASA EONET para Bolivia"""
    
    # Buscar en caché (para no saturar la API)
    cache_key = 'nasa_eventos_bolivia'
    eventos = cache.get(cache_key)
    
    if eventos is None:
        try:
            # API de EONET de la NASA
            url = "https://eonet.gsfc.nasa.gov/api/v3/events"
            params = {
                'status': 'open',
                'limit': 100
            }
            
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            # Bolivia está entre: Latitud: -22.5 a -9.5, Longitud: -69.5 a -57.5
            eventos_bolivia = []
            
            for event in data.get('events', []):
                for geometry in event.get('geometry', []):
                    coordinates = geometry.get('coordinates', [])
                    if coordinates:
                        lon, lat = coordinates[0], coordinates[1]
                        # Verificar si está dentro del área de Bolivia
                        if -69.5 <= lon <= -57.5 and -22.5 <= lat <= -9.5:
                            eventos_bolivia.append({
                                'id': event.get('id'),
                                'title': event.get('title'),
                                'description': event.get('description', 'Evento natural'),
                                'category': event.get('categories', [{}])[0].get('title', 'Desconocido'),
                                'latitude': lat,
                                'longitude': lon,
                                'date': geometry.get('date', ''),
                                'link': f"https://eonet.gsfc.nasa.gov/api/v3/events/{event.get('id')}"
                            })
                            break
            
            # Si no hay eventos en Bolivia
            if not eventos_bolivia:
                eventos_bolivia = []
            
            eventos = eventos_bolivia
            cache.set(cache_key, eventos, 3600)  # Caché por 1 hora
            
        except Exception as e:
            print(f"Error NASA API: {e}")
            eventos = []
    
    return JsonResponse(eventos, safe=False)

def api_satelite_nasa(request):
    """Obtiene capas satelitales de la NASA GIBS"""
    
    # Capas satelitales disponibles de la NASA
    capas = {
        'fires_current': {
            'nombre': '🔥 Incendios activos (VIIRS - Tiempo Real)',
            'url': 'https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi',
            'layer': 'VIIRS_SNPP_Clean_Infrared_Compatible_Fires_375m_NRT',
            'formato': 'image/png',
            'visible': True,
            'descripcion': 'Detección de incendios activos en las últimas 24 horas'
        },
        'modis_fires': {
            'nombre': '🔥 Incendios MODIS (Histórico)',
            'url': 'https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi',
            'layer': 'MODIS_Terra_Clean_Infrared_Compatible_Fires_375m_NRT',
            'formato': 'image/png',
            'visible': False,
            'descripcion': 'Detección de incendios vía satélite MODIS'
        },
        'true_color': {
            'nombre': '🛰️ Color Real (MODIS - Últimas 24h)',
            'url': 'https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi',
            'layer': 'MODIS_Terra_CorrectedReflectance_TrueColor',
            'formato': 'image/png',
            'visible': False,
            'descripcion': 'Imagen satelital en color real de Bolivia'
        },
        'ndvi': {
            'nombre': '🌿 Vegetación (NDVI) - Salud de cultivos',
            'url': 'https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi',
            'layer': 'MODIS_Terra_NDVI_8Day',
            'formato': 'image/png',
            'visible': False,
            'descripcion': 'Índice de vegetación para monitoreo agrícola'
        },
        'land_surface_temp': {
            'nombre': '🌡️ Temperatura superficial (Día)',
            'url': 'https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi',
            'layer': 'MODIS_Terra_Land_Surface_Temp_Day',
            'formato': 'image/png',
            'visible': False,
            'descripcion': 'Temperatura de la superficie terrestre'
        },
        'clouds': {
            'nombre': '☁️ Cobertura de nubes',
            'url': 'https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi',
            'layer': 'MODIS_Terra_Cloud_Fraction_Day',
            'formato': 'image/png',
            'visible': False,
            'descripcion': 'Porcentaje de cobertura nubosa'
        },
        'aerosols': {
            'nombre': '🌫️ Aerosoles (Calidad del aire)',
            'url': 'https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi',
            'layer': 'MODIS_Terra_Aerosol_Optical_Depth',
            'formato': 'image/png',
            'visible': False,
            'descripcion': 'Partículas en suspensión en la atmósfera'
        },
        'snow_cover': {
            'nombre': '❄️ Cobertura de nieve',
            'url': 'https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi',
            'layer': 'MODIS_Terra_Snow_Cover',
            'formato': 'image/png',
            'visible': False,
            'descripcion': 'Nieve en la cordillera de los Andes'
        }
    }
    
    return JsonResponse(capas, safe=False)
# ============================================
# METADATOS Y TRAZABILIDAD - NUEVAS FUNCIONES
# ============================================

def api_metadatos(request):
    """Devuelve metadatos de todas las capas disponibles"""
    from .models import MetadatoCapa
    from django.core.serializers import serialize
    import json
    
    metadatos = MetadatoCapa.objects.all()
    data = []
    for m in metadatos:
        data.append({
            'id': m.id,
            'nombre_capa': m.nombre_capa,
            'titulo': m.titulo,
            'descripcion': m.descripcion,
            'fuente': m.fuente,
            'fecha_publicacion': m.fecha_publicacion.strftime('%Y-%m-%d'),
            'fecha_actualizacion': m.fecha_actualizacion.strftime('%Y-%m-%d'),
            'resolucion': m.resolucion,
            'responsable': m.responsable
        })
    
    return JsonResponse(data, safe=False)

def api_carga_logs(request):
    """Devuelve historial de cargas (solo admin)"""
    if not request.user.is_staff:
        return JsonResponse({'error': 'No autorizado'}, status=403)
    
    from .models import CargaLog
    logs = CargaLog.objects.all().order_by('-fecha_subida')[:50]
    data = []
    for log in logs:
        data.append({
            'archivo': log.archivo_nombre,
            'usuario': log.usuario,
            'estado': log.estado,
            'fecha': log.fecha_subida.strftime('%Y-%m-%d %H:%M'),
            'mensaje': log.validacion_mensaje,
            'registros': log.registros_afectados
        })
    
    return JsonResponse(data, safe=False)

def api_staging_validate(request):
    """Valida datos en área de staging antes de publicar"""
    import json
    from .models import StagingData, CargaLog
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'No autorizado'}, status=401)
    
    try:
        data = json.loads(request.body)
        archivo_nombre = data.get('archivo_nombre', '')
        contenido = data.get('contenido', {})
        categoria = data.get('categoria', '')
        
        # Validaciones
        errores = []
        
        # Validar estructura básica
        if 'type' not in contenido:
            errores.append('El archivo debe tener un campo "type"')
        
        if contenido.get('type') != 'FeatureCollection':
            errores.append('El archivo debe ser un FeatureCollection')
        
        if 'features' not in contenido:
            errores.append('El archivo debe tener un array "features"')
        
        # Validar cada feature
        registros_validos = 0
        registros_invalidos = 0
        
        for feature in contenido.get('features', []):
            if 'geometry' in feature and 'properties' in feature:
                registros_validos += 1
            else:
                registros_invalidos += 1
        
        if registros_validos == 0:
            errores.append('No hay geometrías válidas en el archivo')
        
        # Guardar en staging
        staging = StagingData.objects.create(
            usuario=request.user.username,
            archivo_nombre=archivo_nombre,
            contenido_json=contenido,
            categoria=categoria,
            estado_validacion='approved' if not errores else 'rejected',
            errores_validacion='; '.join(errores),
            registros_validos=registros_validos,
            registros_invalidos=registros_invalidos
        )
        
        # Registrar en log
        CargaLog.objects.create(
            usuario=request.user.username,
            archivo_nombre=archivo_nombre,
            archivo_tipo='GeoJSON',
            categoria=categoria,
            estado='approved' if not errores else 'rejected',
            validacion_mensaje='; '.join(errores) if errores else 'Validación exitosa',
            registros_afectados=registros_validos
        )
        
        return JsonResponse({
            'success': len(errores) == 0,
            'errores': errores,
            'registros_validos': registros_validos,
            'registros_invalidos': registros_invalidos,
            'staging_id': staging.id
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def api_staging_publish(request, staging_id):
    """Publica datos desde staging a producción"""
    from .models import StagingData, CargaLog, IndicadorClimatico
    
    if not request.user.is_staff:
        return JsonResponse({'error': 'No autorizado - Se requiere rol administrador'}, status=403)
    
    try:
        staging = StagingData.objects.get(id=staging_id)
        
        if staging.estado_validacion != 'approved':
            return JsonResponse({'error': 'Los datos no han sido validados'}, status=400)
        
        # Procesar y publicar datos
        contenido = staging.contenido_json
        nuevos_registros = 0
        
        for feature in contenido.get('features', []):
            props = feature.get('properties', {})
            # Lógica para guardar según tipo de dato
            # (Adaptar según tu modelo)
            nuevos_registros += 1
        
        # Actualizar estado
        staging.estado_validacion = 'published'
        staging.save()
        
        # Actualizar log
        CargaLog.objects.filter(archivo_nombre=staging.archivo_nombre, estado='approved').update(
            estado='published',
            fecha_publicacion=timezone.now()
        )
        
        return JsonResponse({
            'success': True,
            'publicados': nuevos_registros,
            'mensaje': f'Se publicaron {nuevos_registros} registros'
        })
        
    except StagingData.DoesNotExist:
        return JsonResponse({'error': 'Staging no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)