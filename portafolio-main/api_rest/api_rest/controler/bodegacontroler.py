from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from api_rest.business.bodegabusiness import findAll, create, findbyid, deletebyid, update

@api_view(['GET','POST', 'PUT'])
def bodega(request):
    if request.method == 'GET':
        return findAll(request)
    if request.method == 'POST':
        return create(request)
    if request.method == 'PUT':
        return update(request)

@api_view(['GET','DELETE'])
def bodegabyid(request, id):
    if request.method == 'GET':
        return findbyid(request, id)
    if request.method == 'DELETE':
        return deletebyid(request, id)






