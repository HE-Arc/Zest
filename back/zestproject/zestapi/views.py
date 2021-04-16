import shortuuid
from django.contrib.auth.models import User
from django.db.models import Q
from django.http.response import (JsonResponse)
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Booking, Ressource
from .permissions import IsOwnerOrAdmin, IsOwnerOrReadOnly
from .serializers import (BookingActionSerializer, RessourceSerializer,
                          UserSerializer)

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['user'] = UserSerializer(self.user).data
        
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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
    
    @action(methods=['patch'], detail=False, url_path="profile") 
    def user_patch(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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

    @action(methods=['post'], detail=True,  permission_classes=[permissions.IsAuthenticated], url_path="bookings") 
    def booking_add(self, request, share_id, *args, **kwargs):
        resource = get_object_or_404(Ressource, share_id=share_id)
        
        data=request.data
        data['ressource'] = resource.id
        
        serializer = BookingActionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save(user=request.user, ressource=resource)
        
        return Response(serializer.data)

    #no decorator cause it's a nested viewset
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

    #no decorator cause it's a nested viewset
    def booking_delete(self, request, share_id, booking):
        booking = get_object_or_404(Booking, user=request.user, pk=booking)
        booking.delete()
        return Response({'detail': 'Operation success'}, status=status.HTTP_204_NO_CONTENT)


def index(request):
    return JsonResponse("index", safe=False)
