import base64

from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from django.core.files.base import ContentFile
from rest_framework.exceptions import ValidationError

from users.models import User
from pets.models import Pet


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class PetSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False, allow_null=True,)

    class Meta:
        model = Pet
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    pets = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_pets(self, obj):
        pets = Pet.objects.filter(owner=obj,)
        serializer = PetSerializer(pets, many=True,)
        return serializer.data
