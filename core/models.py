from django.db import models

class InformacoesDoSiteDeCarnaval(models.Model):
    primeiro_dia_de_carnaval=models.DateField(default='2022-05-15')
    titulo01=models.CharField(max_length=45)
    titulo02=models.CharField(max_length=45)
    texto02=models.TextField()

class AgendaCarnaval(models.Model):
    data=models.DateField()
    dia=models.CharField(max_length=8, default='')
    titulo=models.CharField(max_length=40)
    hora=models.CharField(max_length=5)
    local=models.CharField(max_length=40)

#class AgramiacaoCArnaval(models.Model):
#img
#escola
#texto