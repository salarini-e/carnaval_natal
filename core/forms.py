from django import forms
from django.forms import ModelForm
from .models import AgendaCarnaval, InformacoesDoSiteDeCarnaval

class InformacoesForm(ModelForm):
    class Meta:
        model = InformacoesDoSiteDeCarnaval        
        fields= '__all__'

class AgendaForm(ModelForm):
    class Meta:
        model=AgendaCarnaval
        fields='__all__'