from typing import cast
from api_rest.models.models import Usuarios
from django.http import JsonResponse, HttpResponse
from rest_framework import status
import json



def findAll(request):
    try: 
        usuarioss = Usuarios.objects.all().order_by('id_usuario')
        return JsonResponse(list(usuarioss.values()), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Usuarios.DoesNotExist as err:
        response = HttpResponse('Error al buscar los usuarios')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def create(request):
    
    try:
        usuarios = json.loads(request.body.decode('utf-8'))
        print('usuarios -> {0}'.format(usuarios))
        newusuarios = Usuarios(
            id_usuario = usuarios.get('id_usuario'),
            nombre = usuarios.get('nombre'),
            contrasena = usuarios.get('contrasena')
        )
        newusuarios.save()
        newusuarios = Usuarios.objects.get(nombre=newusuarios.nombre)
        return JsonResponse(newusuarios.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def findbyid(request, id):
    try: 
        usuarios = Usuarios.objects.get(id_usuario=id)
        return JsonResponse(usuarios.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Usuarios.DoesNotExist as err:
        response = HttpResponse('Error al buscar los usuarios')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def deletebyid(request, id):
    try: 
        usuarios = Usuarios.objects.get(id_usuario=id)
        usuarios.delete()
        response = HttpResponse('usuarios eliminada.')
        response.status_code = status.HTTP_200_OK
        return response
    except Usuarios.DoesNotExist as err:
        response = HttpResponse('Error al eliminar las usuarios')
        response.status_code = status.HTTP_404_NOT_FOUND
        return response             
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response


def update(request):
    
    try:
        usuarios = json.loads(request.body.decode('utf-8'))
        print('usuarios -> {0}'.format(usuarios))
        usuariosup = Usuarios.objects.get(id_usuario=usuarios.get('id_usuario'))
        usuariosup.nombre = usuarios.get('nombre')
        usuariosup.contrasena = usuarios.get('contrasena')
        usuariosup.save(force_update=True)
        return JsonResponse(usuariosup.json_serializer(), safe=False, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al conectarse a la base de datos.')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response