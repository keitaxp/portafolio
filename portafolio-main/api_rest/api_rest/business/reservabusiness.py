from typing import cast
from api_rest.models.models import Reserva
from api_rest.models.models import Mesa
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        reserva = Reserva.objects.all().order_by('id_reserva')
        return JsonResponse(list(reserva.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Reserva.DoesNotExist as err:
        response = HttpResponse('Error al buscar los reserva')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        reserva = json.loads(request.body.decode('utf-8'))
        print('reserva -> {0}'.format(reserva))

        mesa = Mesa.objects.get(id_mesa=reserva.get('id_mesa'))
        newreserva = Reserva(
             
             id_mesa = mesa,
             rut_cliente = reserva.get('rut_cliente'),
             cantidad_personas = reserva.get('cantidad_personas'),
             fecha = reserva.get('fecha')
        )
        newreserva.save()
        newreserva = Reserva.objects.get(rut_cliente=newreserva.rut_cliente)
        return JsonResponse(newreserva.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        reserva = Reserva.objects.get(id_reserva=id)
        return JsonResponse(reserva.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Reserva.DoesNotExist as err:
        response = HttpResponse('RESERVA no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        reserva = Reserva.objects.get(id_reserva=id)
        reserva.delete()
        response = HttpResponse('reserva eliminado.')
        response.status_code = status.HTTP_200_OK
        return response
    except Reserva.DoesNotExist as err:
        response = HttpResponse('reserva no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        reserva = json.loads(request.body.decode('utf-8'))
        print('reserva -> {0}'.format(reserva))
        reservaup = Reserva.objects.get(id_reserva=reserva.get('id_reserva'))
        mesa = Mesa.objects.get(id_mesa=reserva.get('id_mesa'))
        reservaup.id_mesa = mesa
        reservaup.rut_cliente = reserva.get('rut_cliente')
        reservaup.cantidad_personas = reserva.get('cantidad_personas')
        reservaup.fecha = reserva.get('fecha')

        reservaup.save(force_update=True)
        return JsonResponse(reservaup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response