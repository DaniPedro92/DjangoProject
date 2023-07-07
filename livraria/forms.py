from .models import Livro
from django import forms

class livroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"