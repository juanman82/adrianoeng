# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0010_auto_20150710_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='esp_productos',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='esp_productos',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
