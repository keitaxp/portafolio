from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from api_rest.business.receta_pedidobusiness import findAll, create, findbyid, deletebyid

@api_view(['GET','POST', 'PUT'])
def receta_pedido(request):
    if request.method == 'GET':
        return findAll(request)
    if request.method == 'POST':
        return create(request)

@api_view(['GET','DELETE'])
def receta_pedidobyid(request, id):
    if request.method == 'GET':
        return findbyid(request, id)
    if request.method == 'DELETE':
        return deletebyid(request, id)



