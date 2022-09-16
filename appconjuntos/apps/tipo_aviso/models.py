from django.db import models
from django.utils import timezone

#from simple_history.models import HistoricalRecords
class TipoAvisoModel(models.Model):
    tipo = models.CharField('Mensaje', max_length = 50,blank=False, null=False, unique=True, default=0)
    is_active = models.BooleanField(null=False, default = True)
    fecha = models.DateTimeField('Fecha', null=False, default=timezone.now)

    
    class Meta:
        verbose_name = 'Tipo_aviso'
        verbose_name_plural = 'Tipo_avisos'
        ordering = ('fecha',)

    #contructor
    def __str__(self):
       return f'{self.tipo}'
