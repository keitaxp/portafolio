from typing import cast
from api_rest.models.models import Proveedor
from api_rest.models.models import Productos
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        productos = Productos.objects.all().order_by('id_producto')
        return JsonResponse(list(productos.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Productos.DoesNotExist as err:
        response = HttpResponse('Error al buscar los productos')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        producto = json.loads(request.body.decode('utf-8'))
        print('producto -> {0}'.format(producto))

        proveedor = Proveedor.objects.get(id_proveedor=producto.get('id_proveedor'))
        newproducto = Productos(
             
             id_proveedor = proveedor,
             nombre_producto = producto.get('nombre_producto'),
             descripcion = producto.get('descripcion')
        )
        newproducto.save()
        newproducto = Productos.objects.get(nombre_producto=newproducto.nombre_producto)
        return JsonResponse(newproducto.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        producto = Productos.objects.get(id_producto=id)
        return JsonResponse(producto.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Productos.DoesNotExist as err:
        response = HttpResponse('Producto no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        producto = Productos.objects.get(id_producto=id)
        producto.delete()
        response = HttpResponse('producto eliminado.')
        response.status_code = status.HTTP_200_OK
        return response
    except Productos.DoesNotExist as err:
        response = HttpResponse('Producto no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        producto = json.loads(request.body.decode('utf-8'))
        print('producto -> {0}'.format(producto))
        productoup = Productos.objects.get(id_producto=producto.get('id_producto'))
        proveedor = Proveedor.objects.get(id_proveedor=producto.get('id_proveedor'))
        productoup.id_proveedor = proveedor
        productoup.nombre_producto = producto.get('nombre_producto')
        productoup.descripcion = producto.get('descripcion')

        productoup.save(force_update=True)
        return JsonResponse(productoup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response