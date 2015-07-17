# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0002_auto_20150710_1210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='esp_contacto',
            options={'verbose_name_plural': 'Contacto'},
        ),
        migrations.AlterModelOptions(
            name='esp_inicio',
            options={'verbose_name_plural': 'Inicio'},
        ),
        migrations.AlterModelOptions(
            name='esp_nosotros',
            options={'verbose_name_plural': 'Nosotros'},
        ),
    ]
