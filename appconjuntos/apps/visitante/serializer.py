from rest_framework import serializers
from .models import VisitanteModel

class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitanteModel
        fields = '__all__'
        #exclude = ('fecha','fk_casillero', 'fk_persona', 'is_validcode' 'fk_usuario_recibe')