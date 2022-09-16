from rest_framework import serializers
from .models import VehiculoModel

class Vehiculoerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoModel
        fields = '__all__'
        #exclude = ('fecha','fk_casillero', 'fk_persona', 'is_validcode' 'fk_usuario_recibe')