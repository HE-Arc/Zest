from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import RessourceViewSet, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

ressource_list = RessourceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
ressource_detail = RessourceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

ressource_participate_list = RessourceViewSet.as_view({
    'post': 'participate_add'
})

ressource_participate_detail = RessourceViewSet.as_view({
    'patch': 'participate_patch',
    'delete': 'participate_delete'
})

urlpatterns = [
    path('', views.index, name='home'),

    path('ressources', ressource_list, name='ressource-list'),
    path('ressources/<int:pk>', ressource_detail, name='ressource-detail'),
    path('ressources/<int:pk>/participants', ressource_participate_list, name='ressource-participant-list'),
    path('ressources/<int:pk>/participants/<int:participant>', ressource_participate_detail, name='ressource-participant-detail'),
    
    path('users', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),

    # AUTH JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)