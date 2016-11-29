from django.contrib import admin

from .models import Ingresos, Gastos, Tipo

admin.site.register(Ingresos)
admin.site.register(Gastos)
admin.site.register(Tipo)