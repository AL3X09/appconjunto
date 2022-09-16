from django.db import models
from django.utils import timezone

from ..propiedad.models import PropiedadModel

class VisitanteModel(models.Model):
    nombres = models.CharField('Nombres', max_length = 255, null = False)
    apellidos = models.CharField('Apellidos', max_length = 255, null = False)
    placas = models.CharField('Placas', max_length = 5, null = False)
    telefono = models.CharField('Télefono', max_length = 15, null = True)
    comentarios = models.CharField('Detalles', max_length = 300, null = False)
    fk_propiedad = models.ForeignKey(PropiedadModel, on_delete=models.CASCADE, default=1)
    is_vehiculo = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'

    #contructor
    def __str__(self):
       return f'{self.nombres}'
