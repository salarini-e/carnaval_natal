from django.contrib import admin
from .models import AgremiacaoCarnaval, InformacoesDoSiteDeCarnaval, AgendaCarnaval, LegendasFotos
# Register your models here.
admin.site.register(InformacoesDoSiteDeCarnaval)
admin.site.register(AgendaCarnaval)
admin.site.register(LegendasFotos)
admin.site.register(AgremiacaoCarnaval)