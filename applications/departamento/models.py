from enum import unique
from tabnanny import verbose
from django.db import models

# para saber que tipo de model usar para cada tipo de datos a solicitar buscar en google :
# "django models fields type"(en la pag de documentacion de django)
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True, editable=False)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamentos'
        verbose_name_plural = 'Areas de la Empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name')
            
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name