from typing import cast
from api_rest.models.models import Reservado
from api_rest.models.models import Mesa
from api_rest.models.models import Cliente
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        reservado = Reservado.objects.all().order_by('id_reservado')
        return JsonResponse(list(reservado.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Reservado.DoesNotExist as err:
        response = HttpResponse('Error al buscar los reservado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        reservado = json.loads(request.body.decode('utf-8'))
        print('reservado -> {0}'.format(reservado))

        mesa = Mesa.objects.get(id_mesa=reservado.get('id_mesa'))
        cliente = Cliente.objects.get(id_cliente=reservado.get('id_cliente'))
        newreservado = Reservado(
             
             id_mesa = mesa,
             id_reservado= reservado.get('id_reservado'),
             id_cliente = cliente,
             cantidad_personas = reservado.get('cantidad_personas'),
             fecha = reservado.get('fecha')
        )
        newreservado.save()
        newreservado = Reservado.objects.get(id_reservado=newreservado.id_reservado)
        return JsonResponse(newreservado.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        reservado = Reservado.objects.get(id_reservado=id)
        return JsonResponse(reservado.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Reservado.DoesNotExist as err:
        response = HttpResponse('reservado no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        reservado = Reservado.objects.get(id_reservado=id)
        reservado.delete()
        response = HttpResponse('reservado eliminado.')
        response.status_code = status.HTTP_200_OK
        return response
    except Reservado.DoesNotExist as err:
        response = HttpResponse('reservado no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response



def update(request):
    
    try:
        reservado = json.loads(request.body.decode('utf-8'))
        print('reservado -> {0}'.format(reservado))
        reservadoup = Reservado.objects.get(id_reservado=reservado.get('id_reservado'))
        mesa = Mesa.objects.get(id_mesa=reservado.get('id_mesa'))
        cliente = Cliente.objects.get(id_cliente=reservado.get('id_cliente'))
        reservadoup.id_mesa = mesa
        reservadoup.id_cliente = cliente
        reservadoup.cantidad_personas = reservadoup.get('cantidad_personas')
        reservadoup.fecha = reservadoup.get('fecha')
        reservadoup.save(force_update=True)
        return JsonResponse(reservadoup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response