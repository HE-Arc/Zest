from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ressource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.CharField(max_length=255, null=True, blank=True)
    date_start = models.DateField()
    date_end = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    ressource_id = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_ressources_created')
    bookings = models.ManyToManyField(User, through='Booking')

    def __str__(self) -> str:
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}. {self.ressource.name} -> {self.user.username}"