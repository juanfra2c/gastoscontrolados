from django.contrib import admin

from .models import Ingresos, Gastos, TipoGastos, TipoIngresos

admin.site.register(Ingresos)
admin.site.register(Gastos)
admin.site.register(TipoGastos)
admin.site.register(TipoIngresos)