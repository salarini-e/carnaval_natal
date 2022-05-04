from email.mime import image
from django.db import models

class InformacoesDoSiteDeCarnaval(models.Model):
    primeiro_dia_de_carnaval=models.DateField(default='2022-05-15')
    titulo01=models.CharField(max_length=45)
    titulo02=models.CharField(max_length=45)
    texto02=models.TextField()

class AgendaCarnaval(models.Model):
    data=models.DateField()
    dia=models.CharField(max_length=8, default='')
    titulo=models.CharField(max_length=50)
    hora=models.CharField(max_length=5)
    local=models.CharField(max_length=50)

class LegendasFotos(models.Model):
    legenda=models.CharField(max_length=40)
    foto=models.CharField(max_length=10)

class AgremiacaoCarnaval(models.Model):
    img=models.CharField(max_length=54)
    escola=models.CharField(max_length=54)
    texto=models.TextField()

class EventosCarnaval(models.Model):
    img=models.CharField(max_length=54)
    legenda=models.CharField(max_length=54)

class ConcursosCarnaval(models.Model):    
    nome=models.CharField(max_length=54)