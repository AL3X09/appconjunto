from email.policy import default
from time import time
from django.db import models
from  django.utils import timezone
from django.utils.timezone import now

from ..vehiculo.models import VehiculoModel
from ..parqueadero.models import ParqueaderoModel
from ..visitante.models import VisitanteModel

class VehiculoParqueaderoModel(models.Model):
    fk_vehiculo = models.ForeignKey(VehiculoModel, on_delete=models.CASCADE, default=1)
    fk_parqueadero = models.ForeignKey(ParqueaderoModel, on_delete=models.CASCADE, default=1)
    numero_asignado = models.CharField('Número de parqueadero asignado', max_length = 255, null = False)
    comentarios = models.CharField('Detalles', max_length = 255, null = True)
    is_visitante = models.BooleanField(default = False)
    fk_visitante = models.ForeignKey(VisitanteModel, on_delete=models.CASCADE, null = True, blank=True)
    is_active = models.BooleanField(default = True)
    hora_acceso = models.DateTimeField('Hora Ingreso|', null=False, default=now)
    #fecha_inicio_acceso = models.DateTimeField('Fecha', null=False, default=timezone.now)
    #tiempo_dias = models.CharField('Dias permitidos de parqueadero',  max_length = 50, null = False)
    #is_disponible_temp = models.BooleanField(default = True)
    #tiempo_dias_disponible = models.CharField('Dias permitidos de parqueadero',  max_length = 50, null = False) #almaceno si el vehiculo no esta usando el parqueadero o puede cederlo temporalmente a otro vehiculo
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'VehiculoParqueadero'
        verbose_name_plural = 'AuditoriaPedidos'

    #contructor
    def __str__(self):
       return f'{self.comentarios}'
