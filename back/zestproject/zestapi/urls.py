from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import RessourceViewSet, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('ressources', RessourceViewSet.as_view({
                            'get': 'list',
                            'post': 'create'
                        })),
    path('ressources/<str:share_id>', RessourceViewSet.as_view({
                                    'get': 'retrieve',
                                    'put': 'update',
                                    'patch': 'partial_update',
                                    'delete': 'destroy'
                                })),
    path('ressources/<str:share_id>/bookings', RessourceViewSet.as_view({
                                                'post': 'booking_add'
                                            })),
    path('ressources/<str:share_id>/bookings/<int:booking>', RessourceViewSet.as_view({
                                                                'patch': 'booking_patch',
                                                                'delete': 'booking_delete'})),
    path('users', UserViewSet.as_view({
                        'get': 'list',
                        'post': 'create',
                    })),
    path('users/<int:pk>/', UserViewSet.as_view({
                                'get': 'retrieve',
                                'delete': 'destroy'
                            })),

    # AUTH JWT
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)