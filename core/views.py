from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import AgremiacaoCarnaval, InformacoesDoSiteDeCarnaval as Informacoes, LegendasFotos, EventosCarnaval, ConcursosCarnaval
from .models import AgendaCarnaval as Agenda
from datetime import date

import os

from carnaval_natal.settings import BASE_DIR

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .forms import AgremiacaoForm, ConcursosForm, EventosForm, InformacoesForm, AgendaForm, LegendaForm
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
    agremiacoes=AgremiacaoCarnaval.objects.all()
    context={
        'agremiacoes': agremiacoes
    }
    return render(request, 'agremiacao.html', context)

def eventos(request):
    eventos=EventosCarnaval.objects.all()
    context={
        'eventos': eventos
    }
    return render(request, 'eventos.html', context)

def concursos(request):
    concursos=ConcursosCarnaval.objects.all()
    context={
        'concursos': concursos
    }
    return render(request, 'concursos.html', context)

def concursoFotos(request, dir):
    lista=os.listdir(os.path.join(BASE_DIR, 'core/static/img/concursos/'+str(dir)))    
    context={
        'dir': dir,
        'fotos': lista,        
    }
    return render(request, 'concursoFotos.html', context)

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
            form=LegendaForm(request.POST, instance=legenda)
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])      
                os.remove(str(BASE_DIR)+'/core/static/img/fotos/'+nome)                                          
                path = default_storage.save(str(BASE_DIR)+'/core/static/img/fotos/'+str(nome), ContentFile(files[0].read()))                               
                form.save()
                context={
                    'nome': nome,
                    'form': form,
                    'success': True
                }
            except Exception as E:
                print(E)
        return render(request, 'editarFoto.html', context)

@login_required
def listarAgremiacao(request):
    agremiacoes=AgremiacaoCarnaval.objects.all()
    context={
        'agremiacoes': agremiacoes
    }
    return render(request, 'listarAgremiacao.html', context)

@login_required
def addAgremiacao(request):
    context={
        'form': AgremiacaoForm()
    }
    if request.method=='POST':
        try:
            filename=request.POST['escola'].replace(' ', '')+'.jpg'
            files=[]               
            for item in request.FILES:                        
                files.append(request.FILES[item])            
            path = default_storage.save(str(BASE_DIR)+'/core/static/img/agremiacao/'+str(filename), ContentFile(files[0].read()))                                                                               
            agremiacao=AgremiacaoCarnaval(img=request.POST['escola'].replace(' ', '')+'.jpg' ,escola=request.POST['escola'], texto=request.POST['texto'])
            agremiacao.save()
            context={
                'form': AgremiacaoForm(),
                'success': True
            }
        except Exception as E:
            print(E)
    return render(request, 'addAgremiacao.html', context)

@login_required
def editarAgremiacao(request, img): 
        agremiacao=AgremiacaoCarnaval.objects.get(img=img)        
        context={
            'img':img,
            'form': AgremiacaoForm(instance=agremiacao)
        }       
        if request.method == 'POST': 
            form=AgremiacaoForm(request.POST, instance=agremiacao)
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])      
                if len(files)!=0:
                    os.remove(str(BASE_DIR)+'/core/static/img/agremiacao/'+img)                                          
                    path = default_storage.save(str(BASE_DIR)+'/core/static/img/agremiacao/'+str(img), ContentFile(files[0].read()))                               
                form.save()
                context={
                    'img': img,
                    'form': form,
                    'success': True
                }
            except Exception as E:
                print(E)                
        return render(request, 'editarAgremiacao.html', context)


@login_required
def listarEventos(request):
    eventos=EventosCarnaval.objects.all()
    context={
        'eventos': eventos
    }
    return render(request, 'listarEventos.html', context)

@login_required
def addEvento(request):
    context={
        'form': EventosForm()
    }
    if request.method=='POST':
        try:
            filename=request.POST['legenda'].replace(' ', '')+'.jpg'
            files=[]               
            for item in request.FILES:                        
                files.append(request.FILES[item])            
            path = default_storage.save(str(BASE_DIR)+'/core/static/img/eventos/'+str(filename), ContentFile(files[0].read()))                                                                               
            eventos=EventosCarnaval(img=filename, legenda=request.POST['legenda'])
            eventos.save()
            context={
                'form': EventosForm(),
                'success': True
            }
        except Exception as E:
            print(E)
    return render(request, 'addEventos.html', context)

@login_required
def editarEvento(request, img): 
        evento=EventosCarnaval.objects.get(img=img)
        context={
            'img': img,
            'form': EventosForm(instance=evento)
        }       
        if request.method == 'POST': 
            form=EventosForm(request.POST, instance=evento)
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])  
                if len(files)!=0:
                    os.remove(str(BASE_DIR)+'/core/static/img/eventos/'+img)
                    path = default_storage.save(str(BASE_DIR)+'/core/static/img/eventos/'+str(img), ContentFile(files[0].read()))                               
                form.save()
                context={
                    'img': img,
                    'form': form,
                    'success': True
                }
            except Exception as E:
                print(E)
        return render(request, 'editarEvento.html', context)

@login_required
def listarConcursos(request):
    concursos=ConcursosCarnaval.objects.all()
    context={
        'concursos': concursos
    }
    return render(request, 'listarConcursos.html', context)

@login_required
def addConcurso(request):
    context={
        'form': ConcursosForm()
    }
    if request.method=='POST':
        try:
            dirname=request.POST['nome']
            files=[]               
            for item in request.FILES:                        
                files.append(request.FILES[item]) 
            if len(files)!=0:
                os.mkdir(str(BASE_DIR)+'/core/static/img/concursos/'+str(dirname))
                path = default_storage.save(str(BASE_DIR)+'/core/static/img/concursos/'+str(dirname)+'/00.jpg', ContentFile(files[0].read()))                                                                               
                concurso=ConcursosCarnaval(nome=dirname)
                concurso.save()
                context={
                    'form': EventosForm(),
                    'success': True
                }
        except Exception as E:
            print(E)
    return render(request, 'addConcurso.html', context)

@login_required
def editarConcurso(request, dir): 
        concurso=ConcursosCarnaval.objects.get(nome=dir)
        lista=os.listdir(os.path.join(BASE_DIR, 'core/static/img/concursos/'+str(dir)))
        print(lista)
        context={
            'fotos': lista,
            'dir': dir
        }
        if request.method == 'POST':             
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])  
                if len(files)!=0:
                    # os.remove(str(BASE_DIR)+'/core/static/img/concursos/'+str(dir)+'/'+str(len(lista)))
                    if len(lista)<10:
                        path = default_storage.save(str(BASE_DIR)+'/core/static/img/concursos/'+str(dir)+'/0'+str(len(lista))+'.jpg', ContentFile(files[0].read()))                                           
                    else:
                        path = default_storage.save(str(BASE_DIR)+'/core/static/img/concursos/'+str(dir)+'/'+str(len(lista))+'.jpg', ContentFile(files[0].read()))                                              
                context={
                    'fotos': os.listdir(os.path.join(BASE_DIR, 'core/static/img/concursos/'+str(dir))),
                    'dir': dir,                    
                    'success': True
                }
            except Exception as E:
                print(E)
        return render(request, 'editarConcurso.html', context)

@login_required
def editarConcursoFoto(request, dir, foto):         
        context={
            'foto': foto,
            'dir': dir
        }
        if request.method == 'POST':             
            try:
                files=[]               
                for item in request.FILES:                        
                        files.append(request.FILES[item])  
                if len(files)!=0:
                    os.remove(str(BASE_DIR)+'/core/static/img/concursos/'+str(dir)+'/'+str(foto))
                    path = default_storage.save(str(BASE_DIR)+'/core/static/img/concursos/'+str(dir)+'/'+str(foto), ContentFile(files[0].read()))                                                               
                context={
                    'foto': foto,
                    'dir': dir,                    
                    'success': True
                }
            except Exception as E:
                print(E)
        return render(request, 'editarConcursoFoto.html', context)