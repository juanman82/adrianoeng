# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0018_auto_20150715_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esp_nosotros',
            name='contenido',
            field=django_markdown.models.MarkdownField(null=True),
        ),
        migrations.AlterField(
            model_name='esp_nosotros',
            name='descripcion',
            field=django_markdown.models.MarkdownField(null=True),
        ),
        migrations.AlterField(
            model_name='esp_productos',
            name='descripcion',
            field=django_markdown.models.MarkdownField(null=True),
        ),
    ]
