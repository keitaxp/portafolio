from typing import cast
from api_rest.models.models import PedidosProductoIntermedio
from api_rest.models.models import PedidoProducto
from api_rest.models.models import Productos
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        pedidosProductoIntermedio = PedidosProductoIntermedio.objects.all().order_by('id_producto')
        return JsonResponse(list(pedidosProductoIntermedio.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except PedidosProductoIntermedio.DoesNotExist as err:
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
        pedidosProductoIntermedio = json.loads(request.body.decode('utf-8'))
        print('pedidosProductoIntermedio -> {0}'.format(pedidosProductoIntermedio))

        pedido_producto = PedidoProducto.objects.get(id_pedido_producto=pedidosProductoIntermedio.get('id_pedido_producto'))
        Producto = Productos.objects.get(id_producto=pedidosProductoIntermedio.get('id_producto'))
        newpedidosProductoIntermedio = PedidosProductoIntermedio(
             
             id_producto = Producto,
             id_pedido_producto = pedido_producto,
             cantidad_producto = pedidosProductoIntermedio.get('cantidad_producto'),
        )
        newpedidosProductoIntermedio.save()
        newpedidosProductoIntermedio = PedidosProductoIntermedio.objects.get(cantidad_producto=newpedidosProductoIntermedio.cantidad_producto)
        return JsonResponse(newpedidosProductoIntermedio.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        pedidosProductoIntermedio = PedidosProductoIntermedio.objects.get(id_producto_intermedio=id)
        return JsonResponse(pedidosProductoIntermedio.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except PedidosProductoIntermedio.DoesNotExist as err:
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
        pedidosProductoIntermedio = PedidosProductoIntermedio.objects.get(id_producto_intermedio=id)
        pedidosProductoIntermedio.delete()
        response = HttpResponse('producto eliminado.')
        response.status_code = status.HTTP_200_OK
        return response
    except PedidosProductoIntermedio.DoesNotExist as err:
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
        pedidosProductoIntermedio = json.loads(request.body.decode('utf-8'))
        print('pedidosProductoIntermedio -> {0}'.format(pedidosProductoIntermedio))
        pedidosProductoIntermedioup = PedidosProductoIntermedio.objects.get(id_producto_intermedio=pedidosProductoIntermedio.get('id_producto_intermedio'))
        productos = Productos.objects.get(id_producto=pedidosProductoIntermedio.get('id_producto'))
        pedidoProducto = PedidoProducto.objects.get(id_pedido_producto=pedidosProductoIntermedio.get('id_pedido_producto'))
        pedidosProductoIntermedioup.id_producto = productos
        pedidosProductoIntermedioup.id_pedido_producto = pedidoProducto
        pedidosProductoIntermedioup.id_producto_intermedio = pedidosProductoIntermedio.get('id_producto_intermedio')
        pedidosProductoIntermedioup.cantidad_producto = pedidosProductoIntermedio.get('cantidad_producto')

        pedidosProductoIntermedioup.save(force_update=True)
        return JsonResponse(pedidosProductoIntermedioup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response