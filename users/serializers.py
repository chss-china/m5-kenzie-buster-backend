from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150, validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")])
    birthdate = serializers.DateField(allow_null=True, default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=127, write_only=True)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        is_employee = validated_data.get('is_employee', False)

        if is_employee:
            validated_data['is_superuser'] = True

        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150,write_only=True)
    password = serializers.CharField(max_length=127, write_only=True)



 