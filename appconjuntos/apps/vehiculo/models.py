from email.policy import default
from django.db import models
from  django.utils import timezone

from ..person.models import PersonModel
from ..tipo_vehiculo.models import TipoVehiculoModel

class VehiculoModel(models.Model):
    marca = models.CharField('Detalles', max_length = 255, null = False, unique = False)
    anio = models.CharField('Detalles', max_length = 4, null = False, unique = False)
    identificador = models.CharField('Placa/Número identificador', max_length = 4, null = False, unique = False)
    fk_tipo_vehiculo = models.ForeignKey(TipoVehiculoModel, on_delete=models.CASCADE, default=1)
    comentarios = models.CharField('Detalles', max_length = 255, null = False, unique = True)
    fk_persona = models.ForeignKey(PersonModel, on_delete=models.CASCADE, default=1)
    is_acceso_parqueadero = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

    #contructor
    def __str__(self):
       return f'{self.marca}'
