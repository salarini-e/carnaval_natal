# Generated by Django 3.2.13 on 2024-10-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0024_alter_atracaoimages_section_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='atracao',
            name='titulo',
            field=models.TextField(verbose_name='Título'),
        ),
    ]
