from django.shortcuts import render

# Create your views here.
def mostrar_tarefas(request):
    #obter tarefas da base de dados!
    #mostrar o template e enviar as tarefas
    return render(request,"home.html")
