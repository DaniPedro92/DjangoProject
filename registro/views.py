from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registro.models import Pessoa
from .forms import PessoaForm, UserForm
from django.contrib import messages

def registrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro:lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'registro/registration.html', {'form': form})

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'registro/lista_pessoas.html', {'pessoas': pessoas})

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        pessoa_form = PessoaForm(request.POST)

        if user_form.is_valid() and pessoa_form.is_valid():
            user = user_form.save()
            pessoa = pessoa_form.save(commit=False)
            pessoa.user = user
            pessoa.save()
            return redirect('registro:lista_pessoas')
    else:
        user_form = UserForm()
        pessoa_form = PessoaForm()

    return render(request, 'registro/signup.html', {'user_form': user_form, 'pessoa_form': pessoa_form})
