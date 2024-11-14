#Importações de estruturas padrões do Django:
from django.shortcuts import render, redirect
#Importações de estruturas da aplicação:
from natal.models import *

from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Noticia
from .forms import NoticiaForm, ProgramacaoForm, NovaDataForm
from django.contrib import messages
from django.db.models import Count

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
    bannerPrincipalHomeMOBILE = Banner.objects.filter(nome='BannerPrincipalHomeMOBILE').first()
    # PEGAR AS NOTÍCIAS
    ultimas_noticias = Noticia.objects.filter(publicado=True).order_by('-publicado_em')[:4]

    # CARREGAR AS SECTIONS, EXCETO REINO DE NOEL
    sections = Sections.objects.filter(ativa=True).exclude(slug='reinoNoel').order_by('-dt_insercao')

    # No final da view, para pegar diretamente a section com slug "o-reino-de-noel"
    reino_de_noel = Sections.objects.filter(slug='reinoNoel').first()
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
        'sections': sections,
        'bannerPrincipalHomeWeb': bannerPrincipalHomeWeb,
        'bannerPrincipalHomeMOBILE': bannerPrincipalHomeMOBILE,
        'programacao': programacao,
        'parceiros': Parceiro.objects.all(),
        'atracoes': Atracao.objects.all(),
        'testemonios': Testemunho.objects.all(),
        'galeria_images': Galeria.objects.all(),
        'ultimas_noticias': ultimas_noticias,
        'reino_de_noel': reino_de_noel, 
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
    bannerPrincipalReinoNoelMOBILE = Banner.objects.filter(nome='BannerPrincipalReinoNoelMOBILE').first()
    midBanners = AtracaoImages.objects.all().order_by('-id')[:4]  
    midBannersAll = AtracaoImages.objects.all().order_by('-id')  
    descricao = Atracao.objects.filter(slug='reinoNoel').first()
    print("teste", bannerPrincipalReinoNoelMOBILE)
    context={
        'bannerPrincipalReinoNoelWeb': bannerPrincipalReinoNoelWeb,
        'bannerPrincipalReinoNoelMOBILE': bannerPrincipalReinoNoelMOBILE,
        'descricao': descricao,
        'midBanners': midBanners,
        'midBannersAll': midBannersAll
    }
    return render(req,'natal/reinoNoel.html', context)

def decoracoes(req):
    midBanners = AtracaoImages.objects.all().order_by('-id')[:4]  
    midBannersAll = AtracaoImages.objects.all().order_by('-id')  
    descricao = Atracao.objects.filter(slug='decoracoes').first()
    bannerPrincipalDecoracoesWeb = Banner.objects.filter(nome='BannerPrincipalDecoracoesWeb').first()
    bannerPrincipalDecoracoesMOBILE = Banner.objects.filter(nome='BannerPrincipalDecoracoesMOBILE').first()

    context={
        'descricao': descricao,
        'bannerPrincipalDecoracoesWeb': bannerPrincipalDecoracoesWeb,
        'bannerPrincipalDecoracoesMOBILE': bannerPrincipalDecoracoesMOBILE,
        'midBanners': midBanners,
        'midBannersAll': midBannersAll
        
    }

    return render(req, 'natal/decoracoes.html', context)

def desfiles(req):
    midBanners = AtracaoImages.objects.all().order_by('-id')[:4]  
    midBannersAll = AtracaoImages.objects.all().order_by('-id')  
    descricao = Atracao.objects.filter(slug='desfiles').first()
    bannerPrincipalDesfilesWeb = Banner.objects.filter(nome='BannerPrincipalDesfilesWeb').first()
    bannerPrincipalDesfilesMOBILE = Banner.objects.filter(nome='BannerPrincipalDesfilesMOBILE').first()

    context={
        'descricao': descricao,
        'bannerPrincipalDesfilesWeb': bannerPrincipalDesfilesWeb,
        'bannerPrincipalDesfilesMOBILE': bannerPrincipalDesfilesMOBILE,
        'midBanners': midBanners,
        'midBannersAll': midBannersAll
    }
    return render(req, 'natal/desfiles.html', context)

def teatros(req):
    midBanners = AtracaoImages.objects.all().order_by('-id')[:4]  
    midBannersAll = AtracaoImages.objects.all().order_by('-id')  
    descricao = Atracao.objects.filter(slug='teatros').first()
    bannerPrincipalTeatrosWeb = Banner.objects.filter(nome='BannerPrincipalTeatrosWeb').first()
    bannerPrincipalTeatrosMOBILE = Banner.objects.filter(nome='BannerPrincipalTeatrosMOBILE').first()
    context={
        'descricao': descricao,
        'bannerPrincipalTeatrosWeb':bannerPrincipalTeatrosWeb,
        'bannerPrincipalTeatrosMOBILE':bannerPrincipalTeatrosMOBILE,
        'midBanners': midBanners,
        'midBannersAll': midBannersAll
    }
    return render(req, 'natal/teatros.html', context)

def casaPapaiNoel(req):
    midBanners = AtracaoImages.objects.all().order_by('-id')[:4]  
    midBannersAll = AtracaoImages.objects.all().order_by('-id')  
    descricao = Atracao.objects.filter(slug='casaPapaiNoel').first()
    bannerPrincipalCasaPapaiNoelWeb = Banner.objects.filter(nome='BannerPrincipalCasaPapaiNoelWeb').first() 
    bannerPrincipalCasaPapaiNoelMOBILE = Banner.objects.filter(nome='BannerPrincipalCasaPapaiNoelMOBILE').first()
    context={
        'descricao': descricao,
        'bannerPrincipalCasaPapaiNoelWeb':bannerPrincipalCasaPapaiNoelWeb,
        'bannerPrincipalCasaPapaiNoelMOBILE':bannerPrincipalCasaPapaiNoelMOBILE,
        'midBanners': midBanners,
        'midBannersAll': midBannersAll
    }
    return render(req, 'natal/casaPapaiNoel.html', context)

def encantoNatal(req):
    midBanners = AtracaoImages.objects.all().order_by('-id')[:4]  
    midBannersAll = AtracaoImages.objects.all().order_by('-id')  
    descricao = Atracao.objects.filter(slug='encantoNatal').first()
    bannerPrincipalEncantoNatalWeb = Banner.objects.filter(nome='BannerPrincipalEncantoNatalWeb').first()
    bannerPrincipalEncantoNatalMOBILE = Banner.objects.filter(nome='BannerPrincipalEncantoNatalMOBILE').first()
    context={
        'descricao': descricao,
        'bannerPrincipalEncantoNatalWeb':bannerPrincipalEncantoNatalWeb,
        'bannerPrincipalEncantoNatalMOBILE':bannerPrincipalEncantoNatalMOBILE,
        'midBanners': midBanners,
        'midBannersAll': midBannersAll
    }
    return render (req, 'natal/encantoNatal.html', context)



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


def ver_todas_noticias(request):
    noticias = Noticia.objects.filter(publicado=True)

    context= {
        'noticias': noticias
    }
    return render(request, 'natal/noticias.html', context)

# PROGRAMACAO
@login_required
def criar_programacao(request):
    datas = ProgramacaoData.objects.all().order_by('data')
    dias_da_semana = [dia[0] for dia in ProgramacaoData.DIAS_DA_SEMANA]

    if request.method == 'POST':
        if 'nova_data_submit' in request.POST:
            nova_data_form = NovaDataForm(request.POST)
            if nova_data_form.is_valid():
                nova_data_form.save()
                messages.success(request, "Nova data adicionada com sucesso!")
            form = ProgramacaoForm()
        else:
            form = ProgramacaoForm(request.POST)
            nova_data_form = NovaDataForm()
            if form.is_valid():
                programacao = form.save(commit=False)
                programacao.save()
                messages.success(request, "Programação criada com sucesso!")
    else:
        form = ProgramacaoForm()
        nova_data_form = NovaDataForm()

    context = {
        'form': form,
        'nova_data_form': nova_data_form,
        'datas': datas,
        'dias_da_semana': dias_da_semana,
    }

    return render(request, 'natal/criar_programacao.html', context)


def ver_programacao(request):
    datas_eventos = ProgramacaoData.objects.annotate(evento_count=Count('eventos')).filter(evento_count__gt=0)
    context = {
        'datas': datas_eventos,
    }
    return render(request, 'natal/programacao.html', context)