# Generated by Django 3.2.13 on 2024-10-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0028_auto_20241010_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracaoimages',
            name='section_image',
            field=models.ImageField(upload_to='atracoes-images/'),
        ),
    ]