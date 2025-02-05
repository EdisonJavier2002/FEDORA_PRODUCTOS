from django.shortcuts import render, redirect, get_object_or_404
from .models import Consumo, Perfil, Medidor, HistorialPropietario, Comunicado, Socio, Tarifa, Ruta, Recaudacion
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Para los dashboard
from django.db.models import Count, F

# Home
def home(request):
    return render(request,"home.html")

# Dashboard
def dashboard(request):
    # PKI 1 Obtener el conteo agrupado por estado_consumo
    consumos = Consumo.objects.values('estado_consumo').annotate(count=Count('estado_consumo'))

    # PKI 2 Obtener el conteo agrupado por estado_per de la tabla Perfil
    perfiles = Perfil.objects.values('estado_per').annotate(count=Count('estado_per'))

    # PKI 3 Obtener el conteo agrupado por estado_med
    medidores = Medidor.objects.values('estado_med').annotate(count=Count('estado_med'))

    # PKI 4 Obtener los datos del historial de propietario
    historial_data = HistorialPropietario.objects.select_related('fk_id_soc', 'fk_id_med') \
        .values('fk_id_soc__nombres_soc', 'fk_id_med__numero_med', 'fecha_cambio_his', 'estado_his') \
        .order_by('-fecha_cambio_his')[:10]  # Aquí seleccionas el número de registros que desees


    # PKI 5 Obtener el total de recaudaciones agrupadas por año, mes e impuesto
    recaudaciones = (
        Recaudacion.objects
        .annotate(anio=F('fecha_emision_rec__year'), mes=F('fecha_emision_rec__month'), impuesto=F('estado_rec'))
        .values('anio', 'mes', 'impuesto')
        .annotate(total_recaudaciones=Count('id_rec'))
        .order_by('-anio', '-mes')
    )

    # PKI 6 Obtener los socios con más recaudaciones
    socios_recaudaciones = Socio.objects.annotate(total_recaudaciones=Count('recaudacion')).order_by('-total_recaudaciones')[:5]

    # PKI 7 Obtener el conteo agrupado por estado_tar Cantidad de Tarifas Activas e Inactivas
    tarifas = Tarifa.objects.values('estado_tar').annotate(count=Count('estado_tar'))

    # PKI 8 Obtener el conteo de medidores por ruta
    medidores_por_ruta = Ruta.objects.annotate(cantidad=Count('medidor')).values('nombre_rut', 'cantidad')

    # KPI 9 # Obtener el conteo agrupado por estado_rut
    rutas = Ruta.objects.values('estado_rut').annotate(count=Count('estado_rut'))

    # KPI 10 Obtener los últimos 10 comunicados
    comunicados = Comunicado.objects.all().order_by('-fecha_com')[:2]


    return render(request, "dashboard.html",{
        "consumos": consumos,
        "perfiles": perfiles,
        "medidores": medidores,
        "historial_data": historial_data,
        "recaudaciones": recaudaciones,
        "socios_recaudaciones": socios_recaudaciones,
        "tarifas": tarifas, 
        "medidores_por_ruta": medidores_por_ruta,
        "rutas": rutas,
        "comunicados": comunicados,
    })
