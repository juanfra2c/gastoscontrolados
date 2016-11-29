from django import forms
from .models import Ingresos
from .models import Gastos

class IngresosForm(forms.ModelForm):

    class Meta:
        model = Ingresos
        fields = ('concepto', 'fecha','importe','permanente','tipo',)

class GastosForm(forms.ModelForm):

    class Meta:
        model = Gastos
        fields = ('concepto', 'fecha','importe','permanente','tipo',)