from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers

from .models import Ressource, Participate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class ParticipateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participate
        exclude = ['ressource', 'id']
        depth = 1

class ParticipateActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participate
        fields = '__all__'

class RessourceSerializer(serializers.ModelSerializer):
    participants = ParticipateSerializer(source="participate_set", many=True,required=False) # la source est importante, par défaut : tablename + "_set" ou alors définir un nom spécifique
    author = UserSerializer(required=False)

    class Meta:
        model = Ressource
        fields = '__all__'
        extra_kwargs = {'ressource_id': {'required': False}}
        depth = 1
