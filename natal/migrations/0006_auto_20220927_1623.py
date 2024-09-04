# Generated by Django 3.2.13 on 2022-09-27 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('natal', '0005_alter_testemonio_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testemonio',
            name='foto',
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='testemonio',
            name='comentario',
            field=models.TextField(max_length=150),
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galerias_imagens', verbose_name='Imagem da galeria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
