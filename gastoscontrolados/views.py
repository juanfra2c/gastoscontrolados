from django.db.models import Q
from django.shortcuts import render
from .forms import IngresosForm
from .forms import GastosForm
from django.template import RequestContext
from .models import Ingresos
from .models import Gastos
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the gastos index.")
    
def vgastos(request, gastos_id):
    return HttpResponse("You're looking at question %s." % gastos_id)

def vingresos(request):
    ingresos_all = Ingresos.objects.order_by('fecha')
    gastos_all = Gastos.objects.order_by('fecha')
    if request.method == 'POST':
        if 'ing_save' in request.POST:
            formIng = IngresosForm(request.POST)
            if formIng.is_valid():
                formIng.save()
                formIng = IngresosForm()
                formGas = GastosForm()
                return render(request, 'gastoscontrolados/ingreso.html', {'formIng': formIng,'formGas': formGas,'ingresos': ingresos_all,'gastos': gastos_all})    
        if 'gastos_save' in request.POST:
            formGas = GastosForm(request.POST)
            if formGas.is_valid():
                formGas.save()
                formIng = IngresosForm()
                formGas = GastosForm()
                return render(request, 'gastoscontrolados/ingreso.html', {'formIng': formIng,'formGas': formGas,'ingresos': ingresos_all,'gastos': gastos_all})    
    formIng = IngresosForm()
    formGas = GastosForm()
    return render(request, 'gastoscontrolados/ingreso.html', {'formIng': formIng,'formGas': formGas,'ingresos': ingresos_all,'gastos': gastos_all})
        