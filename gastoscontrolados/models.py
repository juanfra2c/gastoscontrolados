from __future__ import unicode_literals

from django.db import models

class TipoGastos(models.Model):
    idTipo = models.IntegerField(default=0)
    descripcion  = models.CharField(max_length=200)

    def __str__(self):
            return self.descripcion

class TipoIngresos(models.Model):
    idTipo = models.IntegerField(default=0)
    descripcion  = models.CharField(max_length=200)

    def __str__(self):
            return self.descripcion


class Ingresos(models.Model):
    concepto = models.CharField(max_length=200)
    fecha = models.DateTimeField('fecha ingreso')
    importe = models.IntegerField(default=0)
    permanente = models.BooleanField(default=0)
    ttipo = models.ManyToManyField(TipoIngresos)

    def __str__(self):
            return self.concepto

class Gastos(models.Model):
    concepto = models.CharField(max_length=200)
    fecha = models.DateField('fecha ingreso')
    importe = models.IntegerField(default=0)
    permanente = models.BooleanField(default=0)
    tipo = models.ManyToManyField(TipoGastos)

    def __str__(self):
            return self.concepto

