from typing import cast
from api_rest.models.models import Finanzas
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        finanzass = Finanzas.objects.all().order_by('id_finanza')
        return JsonResponse(list(finanzass.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Finanzas.DoesNotExist as err:
        response = HttpResponse('Error al buscar los Finanzas')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        finanzas = json.loads(request.body.decode('utf-8'))
        print('finanzas -> {0}'.format(finanzas))
        newfinanzas = finanzas(
            precio = finanzas.get('precio'),
            descripcion = finanzas.get('descripcion'),
            nombre = finanzas.get('nombre')
        )
        newfinanzas.save()
        newfinanzas = Finanzas.objects.get(precio=newfinanzas.precio)
        newfinanzas = Finanzas.objects.get(descripcion=newfinanzas.descripcion)
        newfinanzas = Finanzas.objects.get(nombre=newfinanzas.nombre)
        return JsonResponse(newfinanzas.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        finanzas = Finanzas.objects.get(id_finanza=id)
        return JsonResponse(finanzas.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Finanzas.DoesNotExist as err:
        response = HttpResponse('Error al buscar los finanzas')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        finanzas = Finanzas.objects.get(id_finanza=id)
        finanzas.delete()
        response = HttpResponse('finanzas eliminada.')
        response.status_code = status.HTTP_200_OK
        return response
    except Finanzas.DoesNotExist as err:
        response = HttpResponse('Error al eliminar las finanzas')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        finanzas = json.loads(request.body.decode('utf-8'))
        print('finanzas -> {0}'.format(finanzas))
        finanzasup = Finanzas.objects.get(id_finanza=finanzas.get('id_finanza'))
        finanzasup.precio = finanzas.get('precio')
        finanzasup.descripcion = finanzas.get('descripcion')
        finanzasup.nombre = finanzas.get('nombre')
        finanzasup.save(force_update=True)
        return JsonResponse(finanzasup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response