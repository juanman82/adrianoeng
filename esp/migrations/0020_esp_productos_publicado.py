# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0019_auto_20150715_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='esp_productos',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]
