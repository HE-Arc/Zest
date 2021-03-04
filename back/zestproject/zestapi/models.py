from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=255)
class Ressource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    ressource_id = models.CharField(255)
    participants = models.ManyToManyField(Person, through='Participate')
    user = models.ForeignKey(User) 

class Participate(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


