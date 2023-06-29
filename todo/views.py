from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.
def mostrar_tarefas(request):
    # obter tarefas da base de dados!!
    tarefas = Tarefa.objects.all().order_by('titulo').filter(realizado=False)
    # select * from tarefa where realizado = 0 order by titulo
    # mostrar o template e enviar as tarefas
    return render(request,"todo/home.html", {'tarefas':tarefas})

def inserir_tarefa(request):
    formulario = TarefaForm
    if request.method=="POST":
        formulario = TarefaForm(request.POST)
        formulario.save()
        return redirect(mostrar_tarefas)

    return render(request, "todo/adicionar.html", {'formulario':formulario})
