from email.policy import default
from django.db import models
from  django.utils import timezone

from ..users.models import User
from ..casillero.models import CasilleroModel
from ..person.models import PersonModel

class TipoVehiculoModel(models.Model):
    nombre = models.CharField('Detalles', max_length = 255, null = False, unique = True)
    is_active = models.BooleanField(default = True)
    
    class Meta:
        verbose_name = 'TipoVehiculo'
        verbose_name_plural = 'TipoVehiculos'

    #contructor
    def __str__(self):
       return f'{self.nombre}'
