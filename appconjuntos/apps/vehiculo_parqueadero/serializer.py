from rest_framework import serializers
from .models import VehiculoParqueaderoModel

class VehiculoParqueaderoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoParqueaderoModel
        fields = '__all__'
        #exclude = ('fecha','fk_casillero', 'fk_persona', 'is_validcode' 'fk_usuario_recibe')