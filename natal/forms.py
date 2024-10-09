from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'imagem', 'publicado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }