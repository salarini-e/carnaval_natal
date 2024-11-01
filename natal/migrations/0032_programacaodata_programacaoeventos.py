# Generated by Django 3.2.13 on 2024-11-01 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0031_remove_atracao_subtitulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramacaoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(unique=True)),
                ('dia_da_semana', models.CharField(choices=[('Segunda-feira', 'Segunda-feira'), ('Terça-feira', 'Terça-feira'), ('Quarta-feira', 'Quarta-feira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=15)),
            ],
            options={
                'verbose_name': 'Data da Programação',
                'verbose_name_plural': 'Datas da Programação',
            },
        ),
        migrations.CreateModel(
            name='ProgramacaoEventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('nome', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('programacao_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='natal.programacaodata')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['hora'],
            },
        ),
    ]
