from email.policy import default
from django.db import models
from  django.utils import timezone
from cryptography.fernet import Fernet #https://www.delftstack.com/es/howto/python/python-encrypt-string/

from ..users.models import User
from ..casillero.models import CasilleroModel
from ..person.models import PersonModel

class AuditoriaPedidoModel(models.Model):
    comentarios = models.CharField('Detalles', max_length = 255, null = False, unique = True)
    fecha = models.DateTimeField('Fecha', null=False, default=timezone.now)
    is_esperapedido = models.BooleanField('Se Espera Pedido', default = True)
    is_entregado = models.BooleanField('Pedido Entregado', default = False)
    fk_casillero = models.ForeignKey(CasilleroModel, on_delete=models.CASCADE, default=1)
    fk_persona = models.ForeignKey(PersonModel, on_delete=models.CASCADE, default=1)
    code = models.CharField('Código',max_length = 500,null = False, unique = True, default='code')
    is_validcode = models.BooleanField('Código Valido', default = False)
    fk_usuario_entrega = models.ForeignKey(User, on_delete=models.CASCADE) #usuario celador que entrega
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'AuditoriaPedido'
        verbose_name_plural = 'AuditoriaPedidos'

    #contructor
    def __str__(self):
       return f'{self.comentarios}'
