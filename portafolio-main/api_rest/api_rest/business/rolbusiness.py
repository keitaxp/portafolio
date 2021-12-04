from typing import cast
from api_rest.models.models import Rol
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        rol = Rol.objects.all().order_by('id_rol')
        return JsonResponse(list(rol.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Rol.DoesNotExist as err:
        response = HttpResponse('Error al buscar los rol')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        rol = json.loads(request.body.decode('utf-8'))
        print('rol -> {0}'.format(rol))
        newrol = Rol(
            nombre = rol.get('nombre'),
            descripcion = rol.get('descripcion')
        )
        newrol.save()
        newrol = Rol.objects.get(nombre=newrol.nombre)
        return JsonResponse(newrol.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        rol = Rol.objects.get(id_rol=id)
        return JsonResponse(rol.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Rol.DoesNotExist as err:
        response = HttpResponse('Error al buscar los roles')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        rol = Rol.objects.get(id_rol=id)
        rol.delete()
        response = HttpResponse('rol eliminada.')
        response.status_code = status.HTTP_200_OK
        return response
    except Rol.DoesNotExist as err:
        response = HttpResponse('Error al eliminar las rol')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        rol = json.loads(request.body.decode('utf-8'))
        print('rol -> {0}'.format(rol))
        rolup = Rol.objects.get(id_rol=rol.get('id_rol'))
        rolup.nombre = rol.get('nombre')
        rolup.descripcion = rol.get('descripcion')
        rolup.save(force_update=True)
        return JsonResponse(rolup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response