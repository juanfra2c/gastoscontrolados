from django.db.models import Q
from django.shortcuts import render
from forms import IngresosForm
from forms import GastosForm
from django.template import RequestContext
from .models import Ingresos
from .models import Gastos

def index(request):
    return HttpResponse("Hello, world. You're at the gastos index.")
    
def vgastos(request, gastos_id):
    return HttpResponse("You're looking at question %s." % gastos_id)

def vingresos(request):
    ingresos_all = Ingresos.objects.order_by('fecha')
    gastos_all = Gastos.objects.order_by('fecha')
    if request.method == 'POST':
        formIng = IngresosForm(request.POST)
        formGas = GastosForm(request.POST)
        if formIng.is_valid():
            formIng.save()
            formIng = IngresosForm()
            formGas.save()
            formGas = GastosForm()
            return render(request, 'gastoscontrolados/ingreso.html', {'formIng': formIng,'formGas': formGas,'ingresos': ingresos_all,'gastos': gastos_all})    
    else:
        formIng = IngresosForm()
        formGas = GastosForm()
    return render(request, 'gastoscontrolados/ingreso.html', {'formIng': formIng,'formGas': formGas,'ingresos': ingresos_all,'gastos': gastos_all})