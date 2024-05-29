from .models import Livro
from django import forms

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"

