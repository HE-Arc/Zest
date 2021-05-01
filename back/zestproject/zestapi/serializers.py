from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Ressource, Booking, UserProfile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    picture = serializers.ImageField(source="userprofile.picture", required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'picture']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password = validated_data['password'],
                                        email=validated_data['email'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        profile = UserProfile(user=user)
        profile.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            elif attr == 'userprofile':
                try:
                    profile = UserProfile.objects.get(user=instance)
                except UserProfile.DoesNotExist:
                    profile = UserProfile(user=instance)
                    profile.save()
                profile.picture = validated_data.get('userprofile')['picture']
                profile.save()
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ['ressource']
        depth = 1

class BookingActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class RessourceSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(source="booking_set", many=True,required=False) # la source est importante, par défaut : tablename + "_set" ou alors définir un nom spécifique
    author = UserSerializer(required=False)
    picture = serializers.ImageField(allow_empty_file=True, required=False)

    class Meta:
        model = Ressource
        fields = '__all__'
        extra_kwargs = {'share_id': {'required': False},'date_end': {'required': False}}
        depth = 1
