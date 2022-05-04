from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import InformacoesDoSiteDeCarnaval as Informacoes, LegendasFotos
from .models import AgendaCarnaval as Agenda
from datetime import date

import os

from carnaval_natal.settings import BASE_DIR

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .forms import InformacoesForm, AgendaForm, LegendaForm
def carnaval(request):
    info=Informacoes.objects.get(id=1)
    agenda=Agenda.objects.all().order_by('data')
    today=date.today()
    carnaval=info.primeiro_dia_de_carnaval
    delta=carnaval-today    
    print(today.strftime("%d/%m/%Y"))
    context={
        'info': info,
        'agenda': agenda,
        'dias': delta.days,
    }
    return render(request, 'carnaval.html', context)

def agremiacao(request):
    return render(request, 'agremiacao.html')

def fotos(request):
    try:   
        fotos=os.listdir(os.path.join(BASE_DIR, 'core/static/img/fotos/'))
        legendas=LegendasFotos.objects.all().order_by('foto')
    except:
        fotos=[] 
    context={
        'fotos': legendas
    }
    return render(request, 'fotos.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:                
            context={
                'error': True,
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')

@login_required
def informacoes(request):
    info=Informacoes.objects.get(id=1)
    if request.method=='POST':
        form=InformacoesForm(request.POST, instance=info)
        if form.is_valid():
            form.save()          
            context={
                'form': form,
                'success': True
            }       
            return render(request, 'informacoesCarnaval.html', context)  
    else:
        form=InformacoesForm(instance=info)        
    context={
        'form': form,
    }
    return render(request, 'informacoesCarnaval.html', context)

@login_required
def painel(request):
    return render(request, 'painelCarnaval.html')


@login_required
def listarAgenda(request):
    context={
        'agenda': Agenda.objects.all()
    }
    return render(request, 'listarAgenda.html', context)


@login_required
def editarAgenda(request, id):
    agenda=Agenda.objects.get(id=id)
    if request.method=='POST':
        form=AgendaForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()          
            context={
                'form': form,
                'success': True
            }       
            return render(request, 'editarAgenda.html', context)  
    else:
        form=AgendaForm(instance=agenda)        
    context={
        'form': form,
    }
    return render(request, 'editarAgenda.html', context)

@login_required
def cadastrarAgenda(request):
    if request.method=='POST':
        form=AgendaForm(request.POST)
        if form.is_valid():
            form.save()          
            context={
                'form': form,
                'success': True
            }       
            return render(request, 'editarAgenda.html', context)  
    else:
        form=AgendaForm()        
    context={
        'form': form,
    }
    return render(request, 'editarAgenda.html', context)

@login_required
def listarSlide(request):
    return render(request, 'listarSlide.html')

@login_required
def editarSlide(request, id):
    return render(request, 'editarSlide.html')


@login_required
def editarSlide(request, id):
        if request.method == 'POST': 
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])                
                file_name=str(id)
                os.remove(str(BASE_DIR)+'/core/static/img/slide/'+str(file_name)+".png")
                path = default_storage.save(str(BASE_DIR)+'/core/static/img/slide/'+str(file_name)+".png", ContentFile(files[0].read()))                               
            except Exception as E:
                print(E)
        context={
            'id': id
        }
        return render(request, 'editarSlide.html', context)

@login_required
def listarImagens(request):
    return render(request, 'listarImagens.html')

@login_required
def editarImagens(request, nome):
        context={
            'id': nome
        }
        if request.method == 'POST': 
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])                                
                os.remove(str(BASE_DIR)+'/core/static/img/'+nome)
                path = default_storage.save(str(BASE_DIR)+'/core/static/img/'+nome, ContentFile(files[0].read()))                               
                context={
                    'id': nome,
                    'success': True
                }
            except Exception as E:
                print(E)

        return render(request, 'editarImagem.html', context)

@login_required
def listarFotos(request):
    try:   
        fotos=os.listdir(os.path.join(BASE_DIR, 'core/static/img/fotos/'))
    except:
        fotos=[] 
    context={
        'fotos': fotos
    }
    return render(request, 'listarFotos.html', context)

@login_required
def enviarFoto(request):   
        context={}
        if request.method == 'POST':             
            try:   
                fotos=os.listdir(os.path.join(BASE_DIR, 'core/static/img/fotos/'))
            except:
                fotos=[] 
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])                                                
                legenda=LegendasFotos(legenda=request.POST['legenda'], foto=str(len(fotos))+'.jpg')
                legenda.save()
                path = default_storage.save(str(BASE_DIR)+'/core/static/img/fotos/'+str(len(fotos))+'.jpg', ContentFile(files[0].read()))                               
                context={
                    'success': True
                }
            except Exception as E:
                print(E)
        return render(request, 'enviarFoto.html', context)

@login_required
def editarFoto(request, nome): 
        legenda=LegendasFotos.objects.get(foto=nome)
        context={
            'nome': nome,
            'form': LegendaForm(instance=legenda)
        }       
        if request.method == 'POST': 
            form=LegendaForm(request.POST)
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])      
                os.remove(str(BASE_DIR)+'/core/static/img/fotos/'+nome)                                          
                path = default_storage.save(str(BASE_DIR)+'/core/static/img/fotos/'+str(nome), ContentFile(files[0].read()))                               
                context={
                    'nome': nome,
                    'form': form,
                    'success': True
                }
            except Exception as E:
                print(E)
        return render(request, 'editarFoto.html', context)