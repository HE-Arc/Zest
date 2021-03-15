from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import RessourceViewSet, UserViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .views import MyTokenObtainPairView

urlpatterns = [
    path('ressources', RessourceViewSet.as_view({
                            'get': 'list',
                            'post': 'create'
                        })),
    path('ressources/<int:pk>', RessourceViewSet.as_view({
                                    'get': 'retrieve',
                                    'put': 'update',
                                    'patch': 'partial_update',
                                    'delete': 'destroy'
                                })),
    path('ressources/<int:pk>/bookings', RessourceViewSet.as_view({
                                                'post': 'booking_add'
                                            })),
    path('ressources/<int:pk>/bookings/<int:participant>', RessourceViewSet.as_view({
                                                                'patch': 'booking_patch',
                                                                'delete': 'booking_delete'})),
    path('users', UserViewSet.as_view({
                        'get': 'list',
                        'post': 'create',
                        'patch': 'user_patch'
                    })),
    path('users/<int:pk>/', UserViewSet.as_view({
                                'get': 'retrieve',
                                'delete': 'destroy'
                            })),

    # AUTH JWT
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)