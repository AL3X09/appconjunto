from rest_framework import serializers
from .models import AuditoriaPedidoModel

class AuditoriaPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaPedidoModel
        fields = '__all__'
        #exclude = ('fecha','fk_casillero', 'fk_persona', 'is_validcode' 'fk_usuario_recibe')