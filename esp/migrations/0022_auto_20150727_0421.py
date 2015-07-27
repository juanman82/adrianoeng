# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0021_auto_20150727_0416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esp_nosotros',
            old_name='prodicto1',
            new_name='producto1',
        ),
        migrations.RenameField(
            model_name='esp_nosotros',
            old_name='prodicto2',
            new_name='producto2',
        ),
        migrations.RenameField(
            model_name='esp_nosotros',
            old_name='prodicto3',
            new_name='producto3',
        ),
    ]
