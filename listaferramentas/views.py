from django.shortcuts import redirect, render
from .models import ListaFerramenta, Ferramenta
from .forms import FerramentaForm

def index(request):
    ferramentas = Ferramenta.objects.all().order_by('titulo')
    return render(request, "listaferramentas/index.html", {'ferramentas': ferramentas})

def add(request):
    formulario = FerramentaForm()
    if request.method == "POST":
        formulario = FerramentaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("listaferramentas:index")
    return render(request, "listaferramentas/add.html", {'formulario': formulario})


def edit(request, id):
    ferramenta = Ferramenta.objects.get(pk=id)
    formulario = FerramentaForm(instance=ferramenta)
    if request.method == "POST":
        formulario = FerramentaForm(request.POST, request.FILES, instance=ferramenta)
        if formulario.is_valid():
            formulario.save()
            return redirect("listaferramentas:index")
    return render(request, "listaferramentas/edit.html", {'formulario': formulario})


def delete(request, id):
    ferramenta = Ferramenta.objects.get(pk=id)   
    ferramenta.delete()
    return redirect("listaferramentas:index")
