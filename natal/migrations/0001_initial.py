# Generated by Django 3.2.13 on 2022-09-27 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome do parceiro')),
                ('logo', models.FileField(upload_to='parceiros_logos', verbose_name='Imagem para logo do parceiro')),
                ('site', models.CharField(max_length=50, null=True, verbose_name='URL do site do parceiro')),
            ],
        ),
    ]
