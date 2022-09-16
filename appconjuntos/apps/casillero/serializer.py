from rest_framework import serializers
from .models import CasilleroModel

class CasilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasilleroModel
        fields = '__all__'