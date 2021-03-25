from rest_framework.generics import get_object_or_404
from .models import Booking, Ressource
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed, JsonResponse
from .serializers import UserSerializer, RessourceSerializer, BookingActionSerializer
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
    lookup_field = "share_id"

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(pk=self.request.user.id), share_id=shortuuid.uuid())

    def list(self, request):
        queryset = Ressource.objects.filter(Q(author=User.objects.get(pk=self.request.user.id)) | Q(booking__user=User.objects.get(pk=self.request.user.id))).distinct()
        serializer = RessourceSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False,  permission_classes=[permissions.IsAuthenticated]) 
    def booking_add(self, request, share_id, *args, **kwargs):
        resource = get_object_or_404(Ressource, share_id=share_id)
        serializer = BookingActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, ressource=resource)
        return Response(serializer.data)

    @action(methods=['patch'], detail=True) 
    def booking_patch(self, request, share_id, booking):
        obj = Booking.objects.get(pk=booking)
        print(obj.user, request.user)
        if (obj.user != request.user):
            return Response({'detail': 'You can\'t modify booking from other user'}, status=status.HTTP_401_UNAUTHORIZED)
        
        #cleaning request from attack
        request.data.pop('user', None)
        request.data.pop('ressource', None)

        serializer = BookingActionSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def booking_delete(self, request, share_id, booking):
        booking = get_object_or_404(Booking, user=request.user, pk=booking)
        booking.delete()
        return Response({'detail': 'Operation success'}, status=status.HTTP_204_NO_CONTENT)

def index(request):
    return JsonResponse("index", safe=False)
