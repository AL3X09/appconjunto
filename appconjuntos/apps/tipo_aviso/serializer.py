from xml.dom import ValidationErr
from rest_framework import serializers
from .models import TipoAvisoModel

class TipoAvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAvisoModel
        fields = '__all__'
