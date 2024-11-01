from django import forms
from .models import Noticia, ProgramacaoEventos, ProgramacaoData

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'imagem', 'publicado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProgramacaoForm(forms.ModelForm):
    class Meta:
        model = ProgramacaoEventos
        fields = ['programacao_data', 'hora', 'titulo_evento', 'local', 'descricao', 'publicado']
        widgets = {
            'programacao_data': forms.Select(attrs={'class': 'form-criar-programacao-item-select'}),
            'hora': forms.TextInput(attrs={'class': 'form-criar-programacao-item-select'}),
            'titulo_evento': forms.TextInput(attrs={'class': 'form-criar-programacao-item-select'}),
            'local': forms.TextInput(attrs={'class': 'form-criar-programacao-item-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-criar-programacao-item-select'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
