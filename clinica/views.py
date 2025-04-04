# clinica/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from .forms import ConsultaForm

def listar_medicos(request):
    especialidade_filter = request.GET.get('especialidade', None)
    if especialidade_filter:
        medicos = Medico.objects.filter(especialidade=especialidade_filter)
    else:
        medicos = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')  
    else:
        form = ConsultaForm()
    return render(request, 'form_consulta.html', {'form': form})

def detalhes_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    return render(request, 'detalhes_consulta.html', {'consulta': consulta})