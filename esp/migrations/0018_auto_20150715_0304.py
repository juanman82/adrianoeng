# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0017_esp_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='esp_inicio',
            name='descripcion',
            field=django_markdown.models.MarkdownField(null=True),
        ),
        migrations.AddField(
            model_name='esp_inicio',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='descripcion',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='esp_inicio',
            name='contenido',
            field=django_markdown.models.MarkdownField(null=True),
        ),
    ]
