# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esp_contacto',
            old_name='nommbre',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='esp_inicio',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='esp_nosotros',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]
