from typing import cast
from api_rest.models.models import Receta_pedido
from api_rest.models.models import Receta
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        receta_pedido = Receta_pedido.objects.all().order_by('id_receta_pedido')
        return JsonResponse(list(receta_pedido.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Receta_pedido.DoesNotExist as err:
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
        receta_pedido = json.loads(request.body.decode('utf-8'))
        print('receta_pedido -> {0}'.format(receta_pedido))
        receta = Receta.objects.get(id_receta=receta_pedido.get('id_receta'))

        newreceta_pedido = Receta_pedido(
             
             id_receta = receta
        )
        newreceta_pedido.save()
        newreceta_pedido = Receta_pedido.objects.get(id_receta=newreceta_pedido.id_receta)
        return JsonResponse(newreceta_pedido.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        receta_pedido = Receta_pedido.objects.get(id_receta_pedido=id)
        return JsonResponse(receta_pedido.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Receta_pedido.DoesNotExist as err:
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
        receta_pedido = Receta_pedido.objects.get(id_receta_pedido=id)
        receta_pedido.delete()
        response = HttpResponse('reservado eliminado.')
        response.status_code = status.HTTP_200_OK
        return response
    except Receta_pedido.DoesNotExist as err:
        response = HttpResponse('reservado no encontrado')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


