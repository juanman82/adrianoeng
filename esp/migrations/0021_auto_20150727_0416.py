# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0020_esp_productos_publicado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esp_Ingenieria_servicios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to=b'')),
                ('publicado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Ingenier\xeda de Control',
            },
        ),
        migrations.AlterModelOptions(
            name='esp_productos',
            options={'verbose_name_plural': 'INGENIER\xcdA DE CONTROL'},
        ),
        migrations.RenameField(
            model_name='esp_nosotros',
            old_name='contenido',
            new_name='descripcion2',
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='prodicto1',
            field=django_markdown.models.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='prodicto2',
            field=django_markdown.models.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='prodicto3',
            field=django_markdown.models.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='titulo2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='titulop1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='titulop2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='titulop3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='esp_ingenieria_servicios',
            name='producto',
            field=models.OneToOneField(null=True, to='esp.Esp_productos'),
        ),
    ]
