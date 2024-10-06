#Importações de estruturas padrões do Django:
from django.contrib import admin
from django.urls import path, include
#Importações de estruturas da aplicação:
from . import views

urlpatterns = [
    #path('', views.index),
    path('', views.index, name="home"),
    path('reinoNoel', views.reinoNoel, name='reinoNoel'),
    path('decoracoes', views.decoracoes, name='decoracoes'),
    path('desfiles', views.desfiles, name='desfiles'),
    path('teatros', views.teatros, name='teatros'),
    path('sobre/', views.sobre, name="sobre"),
    path('casaDoPapaiNoel/', views.casaDoPapaiNoel, name="casaPapaiNoel"),
    path('programacao/', views.programacao, name="programacao"),
]
