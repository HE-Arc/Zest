from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import RessourceViewSet


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

ressource_participate_list = RessourceViewSet.as_view({
    'post': 'participate_add'
})

ressource_participate_detail = RessourceViewSet.as_view({
    'patch': 'participate_patch',
    'delete': 'participate_delete'
})

urlpatterns = [
    path('', views.index, name='home'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('ressources', ressource_list, name='ressource-list'),
    path('ressources/<int:pk>', ressource_detail, name='ressource-detail'),
    path('ressources/<int:pk>/participants', ressource_participate_list, name='ressource-participant-list'),
    path('ressources/<int:pk>/participants/<int:participant>', ressource_participate_detail, name='ressource-participant-detail'),
    
    path('users', views.user_create, name='user_create'),
    path('users/<int:id>/', views.user_update, name='user_update')
]

urlpatterns = format_suffix_patterns(urlpatterns)