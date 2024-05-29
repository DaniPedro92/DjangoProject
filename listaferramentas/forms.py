from .models import Ferramenta
from django import forms

class FerramentaForm(forms.ModelForm):
    imagem = forms.ImageField(required=False)

    class Meta:
        model = Ferramenta
        fields = ['titulo', 'ano', 'descricao', 'tipo', 'stock', 'imagem']

