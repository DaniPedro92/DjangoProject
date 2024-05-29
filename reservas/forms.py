from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    quantidade = forms.IntegerField(min_value=1, label="Quantidade")

    class Meta:
        model = Reserva
        fields = ['pessoa', 'ferramenta', 'data_reserva']

