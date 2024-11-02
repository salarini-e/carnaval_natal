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
            'hora': forms.TimeInput(attrs={'class': 'form-criar-programacao-item-select', 'type': 'time'}),
            'titulo_evento': forms.TextInput(attrs={'class': 'form-criar-programacao-item-select'}),
            'local': forms.TextInput(attrs={'class': 'form-criar-programacao-item-select'}),
            'descricao': forms.Textarea(attrs={'class': 'form-criar-programacao-item-select'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        datas_choices = [
            (data.id, f"{data.data.strftime('%d/%m/%Y')} - {data.get_dia_da_semana_display()}")
            for data in ProgramacaoData.objects.all()
        ]
        self.fields['programacao_data'].choices = datas_choices


class NovaDataForm(forms.ModelForm):
    class Meta:
        model = ProgramacaoData
        fields = ['data', 'dia_da_semana']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-criar-programacao-item-select'}),
            'dia_da_semana': forms.Select(attrs={'class': 'form-criar-programacao-item-select'}),
        }