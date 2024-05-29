from django import forms
from django.forms import DateInput
from .models import Pessoa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'data_nascimento': DateInput(attrs={'type': 'date'})
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']