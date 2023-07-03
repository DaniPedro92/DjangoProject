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
        return redirect("todo:listar")
    return render(request, "todo/adicionar.html", {'formulario':formulario})

def eliminar_tarefa(request, id):
    tarefa=Tarefa.objects.filter(pk=id)
    tarefa.delete()
    return redirect("todo:listar")

def editar_tarefa(request, id):
    tarefa = Tarefa.objects.get(pk=id)
    formulario = TarefaForm(instance=tarefa)
    if request.method=="POST":
        formulario = TarefaForm(request.POST, instance=tarefa)
        formulario.save()
        return redirect("todo:listar")
    return render(request, "todo/editar.html", {'formulario':formulario})


