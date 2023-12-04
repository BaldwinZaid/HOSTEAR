from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Datos(models.Model):
    pesticida= models.CharField(_('pesticida'), max_length=255)
    planta= models.CharField(_('planta'), max_length=255)
    plaga= models.CharField(_('plaga'), max_length=255)
    nombre_cientifico= models.CharField(_('cientifico'), max_length=255)
    dosis= models.CharField(_('dosis'), max_length=255)
    informacion= models.CharField(_('info'), max_length=2000)
    etiqueta= models.CharField(_('etiqueta'), max_length=2000)

class UserIP(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address