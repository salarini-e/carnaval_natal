# Generated by Django 3.2.13 on 2024-10-09 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0016_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='sections',
            name='ativa',
            field=models.BooleanField(default=True, verbose_name='Publicado'),
        ),
        migrations.AddField(
            model_name='sections',
            name='dt_insercao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Publicação'),
        ),
    ]