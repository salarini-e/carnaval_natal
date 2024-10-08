from django.db import models

class InformacoesDoSiteDeCarnaval(models.Model):
    primeiro_dia_de_carnaval=models.DateField(default='2022-05-15')
    titulo01=models.CharField(max_length=45)
    titulo02=models.CharField(max_length=45)
    texto02=models.TextField()
    texto03=models.TextField(default='', blank=True)
    titulo03=models.CharField(max_length=45, default='')
    texto04=models.TextField(default='', blank=True)
    texto05=models.TextField(default='', blank=True)

class AgendaCarnaval(models.Model):
    data=models.DateField()
    dia=models.CharField(max_length=8, default='')
    titulo=models.CharField(max_length=80)
    subtitulo=models.CharField(max_length=80, default='', blank=True)
    descricao=models.CharField(max_length=150, default='', blank=True)
    hora=models.CharField(max_length=5)
    local=models.CharField(max_length=50)

class LegendasFotos(models.Model):
    legenda=models.CharField(max_length=40)
    foto=models.CharField(max_length=10)

class AgremiacaoCarnaval(models.Model):
    img=models.ImageField(upload_to='img_agremiacao', verbose_name='img', blank=True, null=True)
    escola=models.CharField(max_length=54)
    texto=models.TextField()

class Evento(models.Model):
    nome_do_evento=models.CharField(max_length=80)

class Fotos_Evento(models.Model):
    evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='img_eventos', verbose_name='img', blank=True, null=True)
    legenda=models.CharField(max_length=54)

class ConcursosCarnaval(models.Model):    
    nome=models.CharField(max_length=54)
    link=models.CharField(max_length=250, blank=True, null=True)

class Fotos_Concurso(models.Model):
    concurso=models.ForeignKey(Evento, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='img_concurso', verbose_name='img', blank=True, null=True)
    legenda=models.CharField(max_length=54)

class Fotos_do_Index(models.Model):
    nome=models.CharField(max_length=54)
    img=models.ImageField(upload_to='img_concurso', verbose_name='img', blank=True, null=True)