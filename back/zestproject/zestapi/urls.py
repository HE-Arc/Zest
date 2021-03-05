from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('ressource/<int:id>/', views.ressource_show, name='ressource_show'),
    path('ressource/my', views.ressource_my, name='ressource_my'),
    path('ressource/create', views.ressource_create, name='ressource_create'),
    path('ressource/<int:id>/update', views.ressource_update, name='ressource_update'),
    path('ressource/<int:id>/delete', views.ressource_delete, name='ressource_delete'),
    
    path('user/create', views.user_create, name='user_create'),
    path('user/<int:id>/update', views.user_update, name='user_update')
]