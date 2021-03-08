from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Ressource, Participate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password = validated_data['password'],
                                        email=validated_data['email'])
        return user

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
