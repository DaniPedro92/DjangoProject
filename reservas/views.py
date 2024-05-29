from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import ReservaForm
from .models import Reserva
from listaferramentas.models import Ferramenta
from registro.models import Pessoa
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login 

@login_required
def lista_reservas(request):
    reservas = Reserva.objects.all()  
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

@login_required
def fazer_reserva(request):
    pessoas = Pessoa.objects.all()
    ferramentas = Ferramenta.objects.all()

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)  
            reserva.pessoa = Pessoa.objects.get(pk=request.POST['pessoa'])  
            ferramenta = Ferramenta.objects.get(pk=request.POST['ferramenta'])
            reserva.ferramenta = ferramenta  
            reserva.save()
            messages.success(request, f"Reserva de {ferramenta} feita com sucesso!")  
            return redirect('reservas:lista_reservas')
    else:
        form = ReservaForm()

    context = {
        'form': form,
        'pessoas': pessoas,
        'ferramentas': ferramentas
    }

    return render(request, 'reservas/fazer_reserva.html', context)





