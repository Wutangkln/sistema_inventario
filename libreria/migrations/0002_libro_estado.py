# Generated by Django 5.1.3 on 2024-11-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='estado',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('No Disponible', 'No disponible')], default='Disponible', max_length=20),
        ),
    ]
