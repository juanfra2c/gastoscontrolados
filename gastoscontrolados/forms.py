from django import forms
from .models import Ingresos
from .models import Gastos
from .models import TipoGastos
from .models import TipoIngresos

class IngresosForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(queryset=TipoIngresos.objects.all())
    class Meta:
        model = Ingresos
        fields = ('concepto', 'fecha','importe','permanente','tipo',)

class GastosForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(queryset=TipoGastos.objects.all())
    class Meta:
        model = Gastos
        fields = ('concepto', 'fecha','importe','permanente','tipo',)

class TipoGastosForm(forms.ModelForm):

    class Meta:
        model = TipoGastos
        exclude = ['idTipo']
        fields = ('descripcion',)