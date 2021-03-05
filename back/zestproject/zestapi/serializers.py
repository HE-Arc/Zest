from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Ressource

class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ressource
        fields = '__all__'
        extra_kwargs = {'ressource_id': {'required': False}, 'author':{'required': False}}

