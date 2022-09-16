from django.db import models
from ..conjunto.models import ConjuntoModel

#from simple_history.models import HistoricalRecords
class PropiedadModel(models.Model):
    interior = models.CharField('Interior o Bloque',max_length = 255,blank=False, null=False, unique=True, default=0)
    n_casa_o_apto = models.CharField('Número o Letra de Interior',max_length = 255, blank=False, null=False, unique=True, default=0)
    t_integrantes = models.IntegerField('Total Integrantes', blank=False, null=False, default=0)
    ninos = models.BooleanField('Hay niños', default = False)
    c_ninos = models.IntegerField('Cantidad de niños', blank=False, null=False, default=0)
    abuelos = models.BooleanField('Hay Personas 3ra edad', default = False)
    c_abuelos = models.IntegerField('Cantidad de abuelos', blank=False, null=False, default=0)
    is_habitada = models.BooleanField('Esta habitada', default = True)
    is_arriendo = models.BooleanField('Esta en arriendo', default = False)
    fk_conjunto = models.ForeignKey(ConjuntoModel, on_delete=models.CASCADE, default=1)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    #contructor
    def __str__(self):
       return f'{self.interior} {self.n_casa_o_apto}'
