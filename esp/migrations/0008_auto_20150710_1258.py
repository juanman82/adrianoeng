# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0007_auto_20150710_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esp_inicio',
            name='contenido',
            field=models.TextField(),
        ),
    ]
