from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import RessourceDetail


urlpatterns = [
    path('', views.index, name='home'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('ressources', RessourceDetail.as_view(), name='ressource_create'),
    path('ressources/<int:id>', RessourceDetail.as_view(), name='ressource_show'),
    path('ressources/<int:id>', RessourceDetail.as_view(), name='ressource_update'),
    path('ressources/<int:id>', RessourceDetail.as_view(), name='ressource_delete'),
    path('ressources/my', views.ressource_my, name='ressource_my'),
    
    path('users', views.user_create, name='user_create'),
    path('users/<int:id>/', views.user_update, name='user_update')
]

urlpatterns = format_suffix_patterns(urlpatterns)