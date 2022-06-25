from re import T
from django.db import models
#
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidads Empleados'
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad
    
    
    
    
# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla empleado"""
    
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) #asi se crea la relacion entre :
    #persona y departamento(que es lo que se solicita)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    Habilidades = models.ManyToManyField(Habilidades)
    hola_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Persona'
        verbose_name_plural = 'Registo de Persona'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name