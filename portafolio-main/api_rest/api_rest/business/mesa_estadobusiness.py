from typing import cast
from api_rest.models.models import Mesa_estado
from api_rest.models.models import Cliente
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        mesa_estado = Mesa_estado.objects.all().order_by('id_mesa_estado')
        return JsonResponse(list(mesa_estado.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Mesa_estado.DoesNotExist as err:
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
        mesa_estado = json.loads(request.body.decode('utf-8'))
        print('mesa_estado -> {0}'.format(mesa_estado))

        cliente = Cliente.objects.get(id_cliente=mesa_estado.get('id_cliente'))
        newmesa_estado = Mesa_estado(
             
             id_cliente = cliente,
             id_mesa_estado = mesa_estado.get('id_mesa_estado'),
             estado = mesa_estado.get('estado')
        )
        newmesa_estado.save()
        newmesa_estado = Mesa_estado.objects.get(estado=newmesa_estado.estado)
        return JsonResponse(newmesa_estado.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        mesa_estado = Mesa_estado.objects.get(id_mesa_estado=id)
        return JsonResponse(mesa_estado.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Mesa_estado.DoesNotExist as err:
        response = HttpResponse('mesa_estado no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        mesa_estado = Mesa_estado.objects.get(id_mesa_estado=id)
        mesa_estado.delete()
        response = HttpResponse('mesa_estado eliminado.')
        response.status_code = status.HTTP_200_OK
        return response
    except Mesa_estado.DoesNotExist as err:
        response = HttpResponse('mesa_estado no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        mesa_estado = json.loads(request.body.decode('utf-8'))
        print('mesa_estado -> {0}'.format(mesa_estado))
        mesa_estadoup = Mesa_estado.objects.get(id_mesa_estado=mesa_estado.get('id_mesa_estado'))
        cliente = Cliente.objects.get(id_cliente=mesa_estado.get('id_cliente'))
        mesa_estadoup.id_cliente = cliente
        mesa_estadoup.id_mesa_estado = mesa_estado.get('id_mesa_estado')
        mesa_estadoup.estado = mesa_estado.get('estado')

        mesa_estadoup.save(force_update=True)
        return JsonResponse(mesa_estadoup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response