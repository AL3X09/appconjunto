from rest_framework import serializers
from .models import AvisoModel

class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvisoModel
        fields = '__all__'