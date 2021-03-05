from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ressource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    ressource_id = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, through='Participate')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_ressources_created')

    def __str__(self) -> str:
        return self.name

class Participate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)