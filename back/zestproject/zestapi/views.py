from functools import partial
from .models import Ressource
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import RessourceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class RessourceDetail(APIView): 
    """
    Retrieve, update or delete a resource instance.
    """
    def get_object(self, id):
        try:
            return Ressource.objects.get(id=id)
        except Ressource.DoesNotExist:
            raise Http404

    def get(self, request, id):
        ressource = self.get_object(id)
        serializer = RessourceSerializer(ressource)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        data['author'] = 1 #FIXME change 1 with current user
        data['ressource_id'] = '1' #FIXME
        serializer = RessourceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, id, format=None):
        ressource = self.get_object(id)
        serializer = RessourceSerializer(ressource, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.data)

    def delete(self, request, id, format=None):
        ressource = self.get_object(id)
        print("delete")
        ressource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
def index(request):
    return JsonResponse("index", safe=False)

def login(request):
    pass

def logout(request):
    pass

def ressource_my(request):
    return HttpResponse("my ressources")

def user_create(request):
    return HttpResponse("create new user")

def user_update(request, id):
    return HttpResponse(f"udate user id: {id}")
