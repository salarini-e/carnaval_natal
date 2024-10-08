# Generated by Django 3.2.13 on 2022-11-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0008_local_programacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='endereco',
            field=models.TextField(max_length=256, verbose_name='Endereço do local'),
        ),
        migrations.AlterField(
            model_name='local',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link do google maps para o local'),
        ),
    ]
