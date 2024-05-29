from django.shortcuts import redirect, render
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
    return render(request, "livraria/add.html", {'formulario':formulario} )


def edit(request, id):
    # obter a informação antiga do livro
    livro1 = Livro.objects.get(pk=id)
    formulario = LivroForm(instance = livro1)
    if request.method=="POST":
        formulario = LivroForm(request.POST, request.FILES, instance=livro1)
        formulario.save()
        return redirect("livraria:index")
    return render(request, "livraria/edit.html", {'formulario': formulario})





def delete(request, id):
    #eliminar o livro com primary key igual ao parâmetro url id
    # livro1 = Livro.objects.get(pk=id)     # dá erro se não encontrar o registo com aquele id!
    livro1 = Livro.objects.filter(pk=id)   
    livro1.delete()
    return redirect("livraria:index")
