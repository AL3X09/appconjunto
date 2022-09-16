from django.db import models
from django.conf import settings
import os
from pathlib import Path

def img_directori(instance, filename):
    #return "D:\pythonAPPS\\appconjuntos\\front_vue\public\img\{0}".format(filename)
    return settings.MEDIA_ROOT + "\img\conjunto\{0}".format(filename)

#from simple_history.models import HistoricalRecords
class ConjuntoModel(models.Model):
    name = models.CharField('Nombre', max_length = 255, null = False, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    telephone = models.CharField('Telefono', max_length = 10, blank = True, null = False)
    logo = models.ImageField('Logo del conjunto', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen = models.ImageField('Imagen del conjunto', upload_to = img_directori, max_length = 255, blank = True, null = True)
    adress = models.CharField('Dirección', max_length = 255, blank = True, null = False)
    about = models.CharField('Acerca de nosotros', max_length = 255, blank = True, null = False)
    eslogan = models.CharField('Eslogan', max_length = 255, blank = True, null = False)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Conjunto'
        verbose_name_plural = 'Conjuntos'

    REQUIRED_FIELDS = ['name', 'email', 'telephone', 'adress']

    #contructor
    def __str__(self):
       return f'{self.name}'
