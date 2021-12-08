from typing import cast
from api_rest.models.models import Mesa
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        mesa = Mesa.objects.all().order_by('id_mesa')
        return JsonResponse(list(mesa.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Mesa.DoesNotExist as err:
        response = HttpResponse('Error al buscar los mesa')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        mesa = json.loads(request.body.decode('utf-8'))
        print('mesa -> {0}'.format(mesa))
        newmesa = Mesa(
            id_mesa = mesa.get('id_mesa'),
            disponibilidad = mesa.get('disponibilidad'),
            capacidad = mesa.get('capacidad')
        )
        newmesa.save()
        newmesa = Mesa.objects.get(id_mesa=newmesa.id_mesa)
        return JsonResponse(newmesa.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        mesa = Mesa.objects.get(id_mesa=id)
        return JsonResponse(mesa.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Mesa.DoesNotExist as err:
        response = HttpResponse('Error al buscar los mesa')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        mesa = Mesa.objects.get(id_mesa=id)
        mesa.delete()
        response = HttpResponse('mesa eliminada.')
        response.status_code = status.HTTP_200_OK
        return response
    except Mesa.DoesNotExist as err:
        response = HttpResponse('Error al eliminar las mesa')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        mesa = json.loads(request.body.decode('utf-8'))
        print('mesa -> {0}'.format(mesa))
        mesaup = Mesa.objects.get(id_mesa=mesa.get('id_mesa'))
        mesaup.disponibilidad = mesa.get('disponibilidad')
        mesaup.capacidad = mesa.get('capacidad')
        mesaup.save(force_update=True)
        return JsonResponse(mesaup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response     