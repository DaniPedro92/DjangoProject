from django.shortcuts import render, redirect
from .models import Livro, Editora
from .forms import LivroForm

# Create your views here.
def index(request):
    #obter todos os livros da BD!
    livros = Livro.objects.all().order_by('titulo')
    return render(request,"livraria/index.html", {'livros':livros})

def add(request):
    formulario = LivroForm
    if request.method=="POST":
        formulario = LivroForm(request.POST, request.FILES)
        formulario.save()
        return redirect("livraria:index")
    return render(request, "livraria/add.html", {'formulario':formulario})