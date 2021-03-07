from .models import Participate, Ressource
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import ParticipateSerializer, RessourceSerializer, ParticipateActionSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Q
import shortuuid
from rest_framework.decorators import action, permission_classes
from rest_framework import status

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

    @action(methods=['post'], detail=False) #FIXME add argument permission_classes=[permissions.IsAuthenticated]
    def participate_add(self, request, *args, **kwargs):
        serializer = ParticipateActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['patch'], detail=True) #FIXME add argument permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def participate_patch(self, request, pk, participant):
        obj = Participate.objects.get(id=participant)
        serializer = ParticipateActionSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['delete'], detail=True) #FIXME add argument permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def participate_delete(self, request,pk,  participant):
        obj = Participate.objects.get(id=participant)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return JsonResponse("index", safe=False)

def login(request):
    pass

def logout(request):
    pass

def user_create(request):
    return HttpResponse("create new user")

def user_update(request, id):
    return HttpResponse(f"udate user id: {id}")
