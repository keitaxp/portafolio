from typing import cast
from api_rest.models.models import Cliente
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        clientes = Cliente.objects.all().order_by('id_cliente')
        return JsonResponse(list(clientes.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Cliente.DoesNotExist as err:
        response = HttpResponse('Error al buscar los clientes')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        cliente = json.loads(request.body.decode('utf-8'))
        print('cliente -> {0}'.format(cliente))
        newcliente = Cliente(
            id_cliente = cliente.get('id_cliente'),
            nombre_cliente = cliente.get('nombre_cliente')
        )
        newcliente.save()
        newcliente = Cliente.objects.get(nombre_cliente=newcliente.nombre_cliente)
        newcliente = Cliente.objects.get(id_cliente=newcliente.id_cliente)
        return JsonResponse(newcliente.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        cliente = Cliente.objects.get(id_cliente=id)
        return JsonResponse(cliente.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Cliente.DoesNotExist as err:
        response = HttpResponse('Error al buscar los clientes')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        cliente = Cliente.objects.get(id_cliente=id)
        cliente.delete()
        response = HttpResponse('cliente eliminada.')
        response.status_code = status.HTTP_200_OK
        return response
    except Cliente.DoesNotExist as err:
        response = HttpResponse('Error al eliminar las cliente')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        cliente = json.loads(request.body.decode('utf-8'))
        print('cliente -> {0}'.format(cliente))
        clienteup = Cliente.objects.get(id_cliente=cliente.get('id_cliente'))
        clienteup.nombre_cliente = cliente.get('nombre_cliente')
        clienteup.save(force_update=True)
        return JsonResponse(clienteup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response