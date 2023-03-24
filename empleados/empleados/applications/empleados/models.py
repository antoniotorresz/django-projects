from django.db import models
from empleados.applications.departamentos.models import Departamento


# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    def __str__(self):
        return self.habilidad

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del empleado'


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre completo', max_length=60, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = ''

    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f'{self.id} - {self.first_name} - {self.last_name} - {self.departamento}'
