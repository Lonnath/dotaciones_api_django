from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core import serializers
from .models import Dotaciones
import json
@csrf_exempt
def dotaciones(request):
    dotaciones_all = serializers.serialize("json", Dotaciones.objects.all())
    if dotaciones_all:
        return JsonResponse({'CODE':1, 'MESSAGE':'OK.', 'DATA' : dotaciones_all})
    else:
        return JsonResponse({'CODE':1, 'MESSAGE':'No existen registros.', 'DATA': ''})
@csrf_exempt
def insertar_dotacion(request):
    jd = json.loads(request.body)
    if jd:
        codigo = jd['codigo'] if 'codigo' in jd else None
        nombre = jd['nombre'] if 'nombre' in jd else None
        tipo = jd['tipo'] if 'tipo' in jd else None
        sistema_operativo = jd['sistema_operativo'] if 'sistema_operativo' in jd else None
        if codigo == None or nombre == None or tipo == None or sistema_operativo == None:
            return JsonResponse({'CODE':2, 'MESSAGE':'Faltan datos', 'DATA':''})
        val_id = list(Dotaciones.objects.filter(codigo=codigo))
        if not val_id:
            insert_method = Dotaciones(codigo, nombre, tipo, sistema_operativo).save()
            return JsonResponse({'CODE':1, 'MESSAGE':'Prueba Insercion', 'DATA':jd})
        else:
            return JsonResponse({'CODE':2, 'MESSAGE':'Maquina ya registrada.', 'DATA':''})
        
    else:
        return JsonResponse({'CODE':2, 'MESSAGE':'Json Vacio', 'DATA':''})
@csrf_exempt
def asignar_dotacion(request):
    jd = json.loads(request.body)
    if jd:
        codigo = jd['codigo'] if 'codigo' in jd else None
        empleado_nombre = jd['empleado_nombre'] if 'empleado_nombre' in jd else None
        empleado_email = jd['empleado_email'] if 'empleado_email' in jd else None
        
        if codigo == None or empleado_nombre == None or empleado_email == None:
            return JsonResponse({'CODE':2, 'MESSAGE':'Faltan datos', 'DATA':''})
        maquina = Dotaciones.objects.get(codigo=codigo)

        if maquina:
            if maquina.fecha_asignado == None:
                maquina.fecha_asignado = datetime.datetime.now().strftime("%Y-%m-%d")
                maquina.empleado_asignado = empleado_nombre
                maquina.empleado_email = empleado_email
                maquina.save()
                return JsonResponse({'CODE':1, 'MESSAGE':'Asignado Correctamente.', 'DATA':''})
            else:
                return JsonResponse({'CODE':2, 'MESSAGE':'Maquina asignada anteriormente.', 'DATA':''})
        else:
            return JsonResponse({'CODE':2, 'MESSAGE':'Maquina no existe.', 'DATA':''})
        
    else:
        return JsonResponse({'CODE':2, 'MESSAGE':'Json Vacio', 'DATA':''})