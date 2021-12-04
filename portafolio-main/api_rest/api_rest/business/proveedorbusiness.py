from typing import cast
from api_rest.models.models import Proveedor
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        proveedor = Proveedor.objects.all().order_by('id_proveedor')
        return JsonResponse(list(proveedor.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Proveedor.DoesNotExist as err:
        response = HttpResponse('Error al buscar los Proveedor')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        proveedor = json.loads(request.body.decode('utf-8'))
        print('proveedor -> {0}'.format(proveedor))
        newproveedor = Proveedor(
            nombre_proveedor = proveedor.get('nombre_proveedor'),
            apellido_proveedor = proveedor.get('apellido_proveedor'),
            rut_proveedor = proveedor.get('rut_proveedor'),
            contacto = proveedor.get('contacto')
            
        )
        newproveedor.save()
        newproveedor = Proveedor.objects.get(nombre_proveedor=newproveedor.nombre_proveedor)
        return JsonResponse(newproveedor.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        proveedor = Proveedor.objects.get(id_proveedor=id)
        return JsonResponse(proveedor.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Proveedor.DoesNotExist as err:
        response = HttpResponse('Error al buscar los proveedor')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        proveedor = Proveedor.objects.get(id_proveedor=id)
        proveedor.delete()
        response = HttpResponse('proveedor eliminada.')
        response.status_code = status.HTTP_200_OK
        return response
    except Proveedor.DoesNotExist as err:
        response = HttpResponse('Error al eliminar las proveedor')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        proveedor = json.loads(request.body.decode('utf-8'))
        print('proveedor -> {0}'.format(proveedor))
        proveedorup = Proveedor.objects.get(id_proveedor=proveedor.get('id_proveedor'))
        proveedorup.nombre_proveedor = proveedor.get('nombre_proveedor')
        proveedorup.apellido_proveedor = proveedor.get('apellido_proveedor')
        proveedorup.rut_proveedor = proveedor.get('rut_proveedor')
        proveedorup.contacto = proveedor.get('contacto')
        proveedorup.save(force_update=True)
        return JsonResponse(proveedorup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response     