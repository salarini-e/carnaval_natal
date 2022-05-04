from django import forms
from django.forms import ModelForm
from .models import AgendaCarnaval, AgremiacaoCarnaval, ConcursosCarnaval, EventosCarnaval, InformacoesDoSiteDeCarnaval, LegendasFotos

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


class AgremiacaoForm(ModelForm):
    class Meta:
        model = AgremiacaoCarnaval
        exclude = ['img']

class EventosForm(ModelForm):
    class Meta:
        model = EventosCarnaval
        exclude = ['img']

class ConcursosForm(ModelForm):
    class Meta:
        model = ConcursosCarnaval  
        fields='__all__'      
