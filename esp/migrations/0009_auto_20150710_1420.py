# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0008_auto_20150710_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esp_productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='esp_contacto',
            options={},
        ),
        migrations.AlterModelOptions(
            name='esp_nosotros',
            options={'verbose_name_plural': 'Inicio'},
        ),
        migrations.AlterField(
            model_name='esp_contacto',
            name='mensaje',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='esp_contacto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='esp_inicio',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='esp_nosotros',
            name='contenido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='esp_nosotros',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
