from __future__ import unicode_literals

from django.db import models

class Ingresos(models.Model):
    concepto = models.CharField(max_length=200)
    fecha = models.DateTimeField('fecha ingreso')
    importe = models.IntegerField(default=0)
    permanente = models.IntegerField(default=0)
    tipo = models.IntegerField(default=0)

    def __str__(self):
            return self.concepto

class Gastos(models.Model):
    concepto = models.CharField(max_length=200)
    fecha = models.DateField('fecha ingreso')
    importe = models.IntegerField(default=0)
    permanente = models.IntegerField(default=0)
    tipo = models.IntegerField(default=0)

    def __str__(self):
            return self.concepto

class Tipo(models.Model):
    idTipo = models.IntegerField(default=0)
    defTipo = models.CharField(max_length=200)