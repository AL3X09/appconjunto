from xml.dom import ValidationErr
from rest_framework import serializers
from .models import NoticiaModel

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticiaModel
        fields = '__all__'
