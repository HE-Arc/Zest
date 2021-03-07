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

urlpatterns = [
    path('', views.index, name='home'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('ressources', ressource_list, name='ressource-list'),
    path('ressources/<int:pk>', ressource_detail, name='ressource-detail'),
    
    path('users', views.user_create, name='user_create'),
    path('users/<int:id>/', views.user_update, name='user_update')
]

urlpatterns = format_suffix_patterns(urlpatterns)