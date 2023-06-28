from django.shortcuts import render
from .models import Tarefa

# Create your views here.
def mostrar_tarefas(request):
    # obter tarefas da base de dados!!
    tarefas = Tarefa.objects.all().order_by('titulo')
    # mostrar o template e enviar as tarefas
    return render(request,"todo/home.html", {'tarefas':tarefas})
