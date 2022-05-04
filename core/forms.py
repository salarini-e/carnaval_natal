from django import forms
from django.forms import ModelForm
from .models import AgendaCarnaval, InformacoesDoSiteDeCarnaval, LegendasFotos

class InformacoesForm(ModelForm):
    class Meta:
        model = InformacoesDoSiteDeCarnaval        
        fields= '__all__'

class AgendaForm(ModelForm):
    class Meta:
        model=AgendaCarnaval
        fields='__all__'

class LegendaForm(ModelForm):
    class Meta:
        model = LegendasFotos
        exclude = ['foto']
