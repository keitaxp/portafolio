from typing import cast
from api_rest.models.models import Bodega
from api_rest.models.models import Productos
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        bodega = Bodega.objects.all().order_by('id_bodega')
        return JsonResponse(list(bodega.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Bodega.DoesNotExist as err:
        response = HttpResponse('Error al buscar los bodega')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        bodega = json.loads(request.body.decode('utf-8'))
        print('bodega -> {0}'.format(bodega))

        productos = Productos.objects.get(id_producto=bodega.get('id_producto'))
        newbodega = Bodega(
             
             id_Producto = productos,
             id_bodega = bodega.get('id_bodega'),
             stock = bodega.get('stock')
        )
        newbodega.save()
        newbodega = Bodega.objects.get(nombre_producto=newbodega.nombre_producto)
        return JsonResponse(newbodega.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        bodega = Bodega.objects.get(id_bodega=id)
        return JsonResponse(bodega.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Bodega.DoesNotExist as err:
        response = HttpResponse('Error al buscar los bodega')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        bodega = Bodega.objects.get(id_bodega=id)
        bodega.delete()
        response = HttpResponse('bodega eliminada.')
        response.status_code = status.HTTP_200_OK
        return response
    except Bodega.DoesNotExist as err:
        response = HttpResponse('Error al eliminar las bodega')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        bodega = json.loads(request.body.decode('utf-8'))
        print('bodega -> {0}'.format(bodega))
        bodegaup = Bodega.objects.get(id_bodega=bodega.get('id_bodega'))
        bodegaup.id_producto = bodega.get('id_producto')
        bodegaup.stock = bodega.get('stock')
        bodegaup.save(force_update=True)
        return JsonResponse(bodegaup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response