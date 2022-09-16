from email.policy import default
from django.db import models
from  django.utils import timezone

class TipoParqueaderoModel(models.Model):
    nombre = models.CharField('Detalles', max_length = 255, null = False, unique = True)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'TipoParqueadero'
        verbose_name_plural = 'TipoParqueaderos'

    #contructor
    def __str__(self):
       return f'{self.nombre}'