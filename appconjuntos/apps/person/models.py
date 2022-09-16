from django.db import models
from ..propiedad.models import PropiedadModel
from ..users.models import User

#from simple_history.models import HistoricalRecords
class PersonModel(models.Model):
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    telephone = models.CharField('Télefono', max_length = 10, blank = True, null = True)
    fk_propiedad = models.ForeignKey(PropiedadModel, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    is_propietario = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    #contructor
    def __str__(self):
       return f'{self.name} {self.last_name}'
