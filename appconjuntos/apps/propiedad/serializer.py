from rest_framework import serializers
from .models import PropiedadModel

class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropiedadModel
        fields = '__all__'