from typing import cast
from api_rest.models.models import Mesas
from api_rest.models.models import Pedido
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        pedido = Pedido.objects.all().order_by('id_pedido')
        return JsonResponse(list(pedido.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Pedido.DoesNotExist as err:
        response = HttpResponse('Error al buscar los pedido')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        pedido = json.loads(request.body.decode('utf-8'))
        print('pedido -> {0}'.format(pedido))

        mesas = Mesas.objects.get(id_mesa=pedido.get('id_mesa'))
        newpedido = Pedido(
             
             id_mesa = mesas,
             fecha_pedido = pedido.get('fecha_pedido'),
             precio_total = pedido.get('precio_total')
        )
        newpedido.save()
        newpedido = Pedido.objects.get(precio_total=newpedido.precio_total)
        return JsonResponse(newpedido.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        pedido = Pedido.objects.get(id_pedido=id)
        return JsonResponse(pedido.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Pedido.DoesNotExist as err:
        response = HttpResponse('pedido no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        pedido = Pedido.objects.get(id_pedido=id)
        pedido.delete()
        response = HttpResponse('pedido eliminado.')
        response.status_code = status.HTTP_200_OK
        return response
    except Pedido.DoesNotExist as err:
        response = HttpResponse('Pedido no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        pedido = json.loads(request.body.decode('utf-8'))
        print('pedido -> {0}'.format(pedido))
        pedidoup = Pedido.objects.get(id_pedido=pedido.get('id_pedido'))
        mesas = Mesas.objects.get(id_mesa=pedido.get('id_mesa'))
        pedidoup.id_mesa = mesas
        pedidoup.fecha_pedido = pedido.get('fecha_pedido')
        pedidoup.precio_total = pedido.get('precio_total')

        pedidoup.save(force_update=True)
        return JsonResponse(pedidoup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response