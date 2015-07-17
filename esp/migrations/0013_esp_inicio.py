# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0012_delete_esp_inicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esp_inicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('publicado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Inicio',
            },
        ),
    ]
