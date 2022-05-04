from django.urls import path
from . import views

urlpatterns = [
    path('', views.carnaval),
    path('agremiacao/', views.agremiacao),
    path('fotos/', views.fotos),
    path('s/login/', views.login_view),
    path('s/info', views.informacoes),
    path('s/agenda', views.listarAgenda),
    path('s/agenda/cadastrar', views.cadastrarAgenda),
    path('s/agenda/edit/<id>', views.editarAgenda),
    path('s/slide', views.listarSlide),
    path('s/imagens', views.listarImagens),
    path('s/fotos', views.listarFotos),
    path('s/fotos/enviar', views.enviarFoto),
    path('s/slide/edit/<id>', views.editarSlide),
    path('s/imagens/edit/<nome>', views.editarImagens),
    path('s/fotos/edit/<nome>', views.editarFoto),
    path('s/painel', views.painel),
]
