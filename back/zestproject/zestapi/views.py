from functools import partial
from .models import Ressource
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import RessourceSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Q
import shortuuid

# Create your views here.
class RessourceViewSet(viewsets.ModelViewSet):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer
    #permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(pk=1), ressource_id=shortuuid.uuid()) #FIXME with self.request.user

    def list(self, request):
        queryset = Ressource.objects.filter(Q(author=User.objects.get(pk=1)) | Q(participate__user=User.objects.get(pk=1))) #FIXME with self.request.user
        serializer = RessourceSerializer(queryset, many=True)
        return Response(serializer.data)

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
