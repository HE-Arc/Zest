from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return JsonResponse("index", safe=False)

def login(request):
    pass

def logout(request):
    pass

def ressource_show(request, id):
    return HttpResponse(f"ressource id: {id}")

def ressource_my(request):
    return HttpResponse("my ressources")

def ressource_create(request):
    return HttpResponse("create ressource")

def ressource_update(request, id):
    return HttpResponse(f"update ressource id: {id}")

def ressource_delete(request):
    return HttpResponse(f"delete ressource id: {id}")

def user_create(request):
    return HttpResponse("create new user")

def user_update(request, id):
    return HttpResponse(f"udate user id: {id}")
