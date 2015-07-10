# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0009_auto_20150710_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='esp_contacto',
            options={'verbose_name_plural': 'Contacto'},
        ),
        migrations.AlterModelOptions(
            name='esp_nosotros',
            options={'verbose_name_plural': 'Nosotros'},
        ),
        migrations.AlterModelOptions(
            name='esp_productos',
            options={'verbose_name_plural': 'Productos'},
        ),
    ]
