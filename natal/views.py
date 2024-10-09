#Importações de estruturas padrões do Django:
from django.shortcuts import render
#Importações de estruturas da aplicação:
from natal.models import *

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