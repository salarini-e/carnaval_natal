from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Parceiro)
admin.site.register(Evento)
admin.site.register(Testemunho)
admin.site.register(Galeria)
admin.site.register(Local)
admin.site.register(Programacao)
admin.site.register(Parceiro_Casa_Papai_Noel)
<<<<<<< HEAD

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('nome', 'banner_image_display')  # Exibe o nome e a imagem no admin
    search_fields = ('nome',)  # Permite busca pelo nome
    ordering = ('nome',)  # Ordenação padrão por nome

    def banner_image_display(self, obj):
        if obj.banner_image:
            return f'<img src="{obj.banner_image.url}" style="width: 100px; height: auto;">'
        return "Sem imagem"
    banner_image_display.allow_tags = True
    banner_image_display.short_description = 'Imagem'
=======
admin.site.register(Noticia)
>>>>>>> 7cad6255b23cf8156051f49b958d394a1db6f4c8
