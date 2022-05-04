from django.urls import path
from . import views

urlpatterns = [
    path('', views.carnaval),
    path('agremiacao/', views.agremiacao),
    path('eventos/', views.eventos),
    path('concursos/', views.concursos),
    path('concursos/<dir>', views.concursoFotos),
    path('fotos/', views.fotos),
    
    path('s/login/', views.login_view),
    
    path('s/info', views.informacoes),
    
    path('s/slide', views.listarSlide),
    path('s/slide/edit/<id>', views.editarSlide),

    path('s/imagens', views.listarImagens),
    path('s/imagens/edit/<nome>', views.editarImagens),

    path('s/agenda', views.listarAgenda),
    path('s/agenda/cadastrar', views.cadastrarAgenda),
    path('s/agenda/edit/<id>', views.editarAgenda),

    path('s/fotos', views.listarFotos),
    path('s/fotos/enviar', views.enviarFoto),
    path('s/fotos/edit/<nome>', views.editarFoto),

    path('s/agremiacoes', views.listarAgremiacao),
    path('s/agremiacoes/add', views.addAgremiacao),
    path('s/agremiacao/edit/<img>', views.editarAgremiacao),
    
    path('s/eventos', views.listarEventos),
    path('s/eventos/add', views.addEvento),
    path('s/eventos/edit/<img>', views.editarEvento),

    path('s/concursos', views.listarConcursos),
    path('s/concursos/add', views.addConcurso),
    path('s/concursos/edit/<dir>', views.editarConcurso),
    path('s/concursos/edit/<dir>/<foto>', views.editarConcursoFoto),
    # path('s/concursos/apagar/<nome>', views.editarConcurso),

    path('s/painel', views.painel),
]
