from django.shortcuts import render,redirect
from .models import Livro, Editora
from .forms import livroForm

# Create your views here.

def index(request):
    livros = Livro.objects.all().order_by('titulo')
    return render(request, "livraria/index.html", {'livros': livros})

def add(request):
    formulario = livroForm
    if request.method=="POST":
        formulario = livroForm(request.POST, request.FILES)
        formulario.save()
        return redirect("livraria:index")
    return render(request, "livraria/add.html", {'formulario':formulario})

def delete(request, id):
    livro1 = Livro.objects.filter(pk=id)
    livro1.delete()
    return redirect("livraria:index")

def edit(request, id):
    #obter a informação antiga do livro
    livro1 = Livro.objects.get(pk=id)
    formulario = livroForm(instance = livro1)
    if request.method=="POST":
        formulario = livroForm(request.POST, request.FILES, instance=livro1)
        formulario.save()
        return redirect("livraria:index")
    return render(request, "livraria/edit.html",{'formulario': formulario})