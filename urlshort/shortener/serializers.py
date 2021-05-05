""" serializer to convert queryset to native python types """

from rest_framework.serializers import ModelSerializer
from .models import UrlShort


class UrlShortSerializer(ModelSerializer):
    """ Serializer class """

    class Meta:
        model = UrlShort
        fields = '__all__'