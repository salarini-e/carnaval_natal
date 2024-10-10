from django.db import models
from django.contrib.auth.models import User


class Parceiro(models.Model):
    nome=models.CharField(max_length=30, verbose_name="Nome do parceiro")
    logo=models.ImageField(upload_to='parceiros_logos', verbose_name="Imagem para logo do parceiro") 
    site=models.CharField(verbose_name="URL do site do parceiro", max_length=50, null=True)

class Parceiro_Casa_Papai_Noel(models.Model):
    class Meta:
        verbose_name_plural = "Parceiros_Casa_Papai_Noel"

    nome=models.CharField(max_length=30, verbose_name="Nome do parceiro")
    logo=models.ImageField(upload_to='parceiros_logos', verbose_name="Imagem para logo do parceiro") 
    site=models.CharField(verbose_name="URL do site do parceiro", max_length=50, null=True)


class Testemunho(models.Model):
    autor=models.CharField(max_length=50, verbose_name="Nome da pessoa")
    comentario=models.TextField(max_length=150) 

class Galeria(models.Model):
    image = models.ImageField(upload_to='galerias_imagens', verbose_name="Imagem da galeria")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Local(models.Model):
    class Meta:
        verbose_name_plural = "Locais"

    endereco = models.TextField(max_length=256, verbose_name="Endereço do local")
    link = models.URLField(blank=True, null=True, verbose_name="Link do google maps para o local")

    def __str__(self):
        return '%s' % (self.endereco)
        
class Programacao(models.Model):
    class Meta:
        verbose_name_plural = "Programações"
        verbose_name = "Programação"

    hora = models.DateTimeField()
    local = models.ForeignKey(Local,on_delete=models.PROTECT)
    nome = models.CharField(max_length=256, verbose_name="Nome do evento")

    def __str__(self):
        return '%s - %s - %s' % (self.hora, self.local, self.nome)
    

class Banner(models.Model):
    nome = models.CharField(max_length=64, verbose_name='NomeBanner')   
    banner_image=models.ImageField(upload_to='banners/', null=True, blank=True)
    
from django.utils import timezone

class Sections(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(unique=True, max_length=200)
    subtitulo = models.TextField(verbose_name='Subtítulo',null=True, blank=True)
    descricao = models.TextField(verbose_name='Descrição',null=True, blank=True)
    section_image = models.ImageField(upload_to='sections/', null=True, blank=True)
    section_video = models.CharField(max_length=300, verbose_name='Iframe', null=True, blank=True)
    ativa = models.BooleanField(default=True, verbose_name='Ativa')
    dt_insercao = models.DateTimeField(default=timezone.now, verbose_name='Data de Publicação')

class Atracao(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome', null=True, blank=True)
    titulo = models.TextField(verbose_name='Título',null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=200, default='default-slug')
    subtitulo = models.TextField(verbose_name='Subtítulo',null=True, blank=True)
    descricao = models.TextField(verbose_name='Descrição',null=True, blank=True)
    section_video = models.CharField(max_length=300, verbose_name='Iframe', null=True, blank=True)
    section_image = models.ImageField(upload_to='atracoes/', null=True, blank=True)

class AtracaoImages(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome', null=True, blank=True)
    section_image = models.ImageField(upload_to='atracoes-images/')

class Noticia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(unique=True, max_length=200)
    conteudo = models.TextField(verbose_name='Conteúdo', null=True)
    imagem = models.ImageField(upload_to='noticias/%Y/%m/%d/', verbose_name='Imagem', null=True)
    publicado_em = models.DateTimeField(default=timezone.now, verbose_name='Data de Publicação')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')
    publicado = models.BooleanField(default=True, verbose_name='Publicado')

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['-publicado_em']

    def __str__(self):
        return self.titulo

