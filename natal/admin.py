from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Parceiro)
admin.site.register(Testemunho)
admin.site.register(Galeria)
admin.site.register(Local)
admin.site.register(Programacao)
admin.site.register(Parceiro_Casa_Papai_Noel)

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

admin.site.register(Noticia)

class SectionsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'subtitulo', 'descricao', 'section_image', 'section_video')
    search_fields = ('titulo', 'subtitulo', 'descricao', 'slug')
    list_filter = ('titulo', 'subtitulo')
    prepopulated_fields = {'slug': ('titulo',)}
    def section_image_display(self, obj):
        if obj.section_image:
            return f'<img src="{obj.section_image.url}" style="width: 100px; height: auto;">'
        return "Sem imagem"
    
    section_image_display.allow_tags = True  
    section_image_display.short_description = 'Imagem' 
admin.site.register(Sections, SectionsAdmin)


@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'titulo', 'slug', 'atracao_video', 'atracao_image_display')  # Exibe o título, slug, vídeo e imagem
    search_fields = ('nome', 'titulo', 'slug', 'descricao')  # Permite busca por nome, título, slug e descrição
    list_filter = ('titulo',)  # Filtro pelo título
    prepopulated_fields = {'slug': ('titulo',)}  # Gera o slug a partir do título automaticamente

    # Função para exibir a imagem no admin
    def atracao_image_display(self, obj):
        if obj.atracao_image:
            return f'<img src="{obj.atracao_image.url}" style="width: 100px; height: auto;">'
        return "Sem imagem"
    
    atracao_image_display.allow_tags = True  # Permite que o HTML seja renderizado no admin
    atracao_image_display.short_description = 'Imagem'  # Nome da coluna exibida no admin


@admin.register(AtracaoImages)
class AtracaoImagesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'atracaoImage_image_display')  # Exibe o nome e a imagem
    search_fields = ('nome','atracaoImage_image_display')  # Permite busca pelo nome

    # Função para exibir a imagem no admin
    def atracaoImage_image_display(self, obj):
        if obj.atracaoImage_image:  # Usa o campo correto aqui
            # Retorna o HTML da imagem, permitindo exibição na listagem
            return f'<img src="{obj.atracaoImage_image.url}" style="width: 100px; height: auto;">'
        return "Sem imagem"
    
    atracaoImage_image_display.allow_tags = True  # Permite que o HTML seja renderizado no admin
    atracaoImage_image_display.short_description = 'Imagem'  # Nome da coluna exibida no admin