#Importações de estruturas padrões do Django:
from django.shortcuts import render, redirect
#Importações de estruturas da aplicação:
from natal.models import *

from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Noticia
from .forms import NoticiaForm


def programacao(req):
    context={
        'programacao': []
    }
    return render(req, "natal/programacao.html", context)

def index(req):
    import datetime
    
    programacao_=Programacao.objects.all().order_by('hora')
    datas=programacao_.values('hora')

    # CARREGAR OS BANNERS DA HOME
    bannerPrincipalHomeWeb = Banner.objects.filter(nome='BannerPrincipalHomeWeb').first()

    index=[]
    for data in datas:
        index.append(str(data['hora'].date()))
    index=list(dict.fromkeys(index))
    
    programacao=[]
    for i in index:
        programacao.append([datetime.datetime.strptime(i, '%Y-%m-%d'), []])
    for p in programacao_:
        for i in programacao:
            if str(p.hora.date()) == str(i[0].date()):
                i[1].append(p)    

    context = {
        'bannerPrincipalHomeWeb': bannerPrincipalHomeWeb,
        'programacao': programacao,
        'parceiros': Parceiro.objects.all(),
        'eventos': Evento.objects.all(),
        'testemonios': Testemunho.objects.all(),
        'galeria_images': Galeria.objects.all(),
    }
    
    return render(req, "natal/index.html", context)
    
def sobre(req):
    context = {
        'parceiros': Parceiro.objects.all(),
    }
    return render(req, "natal/sobre.html", context)


def casaDoPapaiNoel(req):
    context = {
        'parceiros': Parceiro.objects.all(),
        'parceiros_casa_do_papai_noel': Parceiro_Casa_Papai_Noel.objects.all(),

    }
    return render(req, "natal/casaDoPapaiNoel.html", context)


def reinoNoel(req):
    bannerPrincipalReinoNoelWeb = Banner.objects.filter(nome='BannerPrincipalReinoNoelWeb').first()
    
    context={
        'bannerPrincipalReinoNoelWeb': bannerPrincipalReinoNoelWeb,
    }
    return render(req,'natal/reinoNoel.html', context)

def decoracoes(req):
    bannerPrincipalDecoracoesWeb = Banner.objects.filter(nome='BannerPrincipalDecoracoesWeb').first()
    context={
        'bannerPrincipalDecoracoesWeb': bannerPrincipalDecoracoesWeb,
    }

    return render(req, 'natal/decoracoes.html', context)

def desfiles(req):
    return render(req, 'natal/desfiles.html')

def teatros(req):
    return render(req, 'natal/teatros.html')

def casaPapaiNoel(req):
    return render(req, 'natal/casaPapaiNoel.html')

def encantoNatal(req):
    return render (req, 'natal/encantoNatal.html')



#NOTICIAS

@login_required
def criar_noticia(request):
    
    if request.method == 'POST':
        
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.slug = slugify(noticia.titulo)
            noticia.conteudo = request.POST['conteudo']
            noticia.save()
            return redirect('ver_noticia', slug=noticia.slug)
    else:
        form = NoticiaForm()
    
    return render(request, 'natal/criar_noticia.html', context={'form': form})

def ver_noticia(request, slug):
    noticia = Noticia.objects.get(slug=slug)
    return render(request, 'natal/ver_noticia.html', context={'noticia': noticia})