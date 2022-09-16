from django.db import models
from django.conf import settings
from  django.utils import timezone

from ..users.models import User
from ..tipo_aviso.models import TipoAvisoModel

def img_directori(instance, filename):
    return settings.MEDIA_ROOT + "\\aviso\{0}".format(filename)

#from simple_history.models import HistoricalRecords
class AvisoModel(models.Model):
    descripcion = models.CharField('Descripción', max_length = 255,blank=False, null=False, unique=False, default=0)
    valor = models.IntegerField('Valor', null=False, unique=False, default=0)
    telefono = models.CharField('Teléfono de contacto', max_length = 20, blank=False, null=False, unique=False, default=0)
    imagen_1 = models.ImageField('Imagen 1', upload_to = img_directori, max_length = 255, blank = True, null = False)
    imagen_2 = models.ImageField('Imagen 2', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen_3 = models.ImageField('Imagen 3', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen_4 = models.ImageField('Imagen 4', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen_5 = models.ImageField('Imagen 5', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen_6 = models.ImageField('Imagen 6', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen_7 = models.ImageField('Imagen 7', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen_8 = models.ImageField('Imagen 8', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen_9 = models.ImageField('Imagen 9', upload_to = img_directori, max_length = 255, blank = True, null = True)
    imagen_10 = models.ImageField('Imagen 10', upload_to = img_directori, max_length = 255, blank = True, null = True)
    fk_usuario_aviso = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    fk_tipoaviso = models.ForeignKey(TipoAvisoModel, on_delete=models.CASCADE, default=1)
    is_approved = models.BooleanField(null=False, default = False)
    is_active = models.BooleanField(null=False, default = True)
    fecha = models.DateTimeField('Fecha', null=False, default=timezone.now)
    
    class Meta:
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'
        ordering = ('fecha',)

    #contructor
    def __str__(self):
       return f'{self.descripcion}'
