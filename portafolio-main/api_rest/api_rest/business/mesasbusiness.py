from typing import cast
from api_rest.models.models import Mesas
from api_rest.models.models import Cliente
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        mesas = Mesas.objects.all().order_by('id_mesa')
        return JsonResponse(list(mesas.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Mesas.DoesNotExist as err:
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
        mesas = json.loads(request.body.decode('utf-8'))
        print('mesas -> {0}'.format(mesas))

        cliente = Cliente.objects.get(id_cliente=mesas.get('id_cliente'))
        newmesas = Mesas(
             
             id_cliente = cliente,
             disponibilidad = mesas.get('disponibilidad'),
             estado_reserva = mesas.get('estado_reserva'),
             numero_mesa = mesas.get('numero_mesa')
        )
        newmesas.save()
        newmesas = Mesas.objects.get(numero_mesa=newmesas.numero_mesa)
        return JsonResponse(newmesas.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        mesas = Mesas.objects.get(id_mesa=id)
        return JsonResponse(mesas.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Mesas.DoesNotExist as err:
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
        mesas = Mesas.objects.get(id_mesa=id)
        mesas.delete()
        response = HttpResponse('mesas eliminado.')
        response.status_code = status.HTTP_200_OK
        return response
    except Mesas.DoesNotExist as err:
        response = HttpResponse('mesas no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        mesas = json.loads(request.body.decode('utf-8'))
        print('mesas -> {0}'.format(mesas))
        mesasup = Mesas.objects.get(id_mesa=mesas.get('id_mesa'))
        cliente = Cliente.objects.get(id_cliente=mesas.get('id_cliente'))
        mesasup.id_cliente = cliente
        mesasup.id_mesa = mesas.get('id_mesa')
        mesasup.disponibilidad = mesas.get('disponibilidad')
        mesasup.estado_reserva = mesas.get('estado_reserva')
        mesasup.numero_mesa = mesas.get('numero_mesa')
        
        mesasup.save(force_update=True)
        return JsonResponse(mesasup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response