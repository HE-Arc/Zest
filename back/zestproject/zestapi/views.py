from .models import Participate, Ressource
from django.contrib.auth.models import User
from django.http.response import HttpResponse, JsonResponse
from .serializers import UserSerializer, RessourceSerializer, ParticipateActionSerializer
from .permissions import IsOwnerOrReadOnly, IsOwnerOrAdmin
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Q
import shortuuid
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (permissions.AllowAny,)

        return super(UserViewSet, self).get_permissions()

class RessourceViewSet(viewsets.ModelViewSet):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(pk=self.request.user.id), ressource_id=shortuuid.uuid())

    def list(self, request):
        queryset = Ressource.objects.filter(Q(author=User.objects.get(pk=self.request.user.id)) | Q(participate__user=User.objects.get(pk=self.request.user.id)))
        serializer = RessourceSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False,  permission_classes=[permissions.IsAuthenticated]) 
    def participate_add(self, request, *args, **kwargs):
        serializer = ParticipateActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['patch'], detail=True) 
    def participate_patch(self, request, pk, participant):
        obj = Participate.objects.get(id=participant)
        serializer = ParticipateActionSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def participate_delete(self, request,pk,  participant):
        obj = Participate.objects.get(id=participant)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return JsonResponse("index", safe=False)

def user_create(request):
    return HttpResponse("create new user")

def user_update(request, id):
    return HttpResponse(f"udate user id: {id}")
