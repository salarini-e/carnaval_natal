# Generated by Django 3.2.13 on 2024-11-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0034_rename_nome_programacaoeventos_titulo_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacaoeventos',
            name='publicado',
            field=models.BooleanField(default=True, verbose_name='Publicado'),
        ),
    ]
