from django.db import models
from django.conf import settings
import os
from  django.utils import timezone


def img_directori(instance, filename):
    return settings.MEDIA_ROOT + "\\noticia\{0}".format(filename)

#from simple_history.models import HistoricalRecords
class NoticiaModel(models.Model):
    titulo = models.CharField('Titulo', max_length = 255, null = False, unique = False)
    subtitulo = models.CharField('Subtitulo', max_length = 255, null = False, unique = False)
    cuerpo = models.CharField('Cuerpo', max_length = 255, null = False, unique = False)
    imagen = models.ImageField('Imagen de la noticia', upload_to = img_directori, max_length = 255, blank = True, null = True)
    url = models.CharField('Url de la noticia', max_length = 400, null = False, unique = False, default= "")
    is_active = models.BooleanField(default = True)
    fecha = models.DateTimeField('Fecha', null=False, default=timezone.now)

    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    #contructor
    def __str__(self):
       return f'{self.titulo}'
