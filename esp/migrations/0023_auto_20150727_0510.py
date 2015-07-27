# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0022_auto_20150727_0421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esp_Servicios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to=b'')),
                ('publicado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.RemoveField(
            model_name='esp_ingenieria_servicios',
            name='producto',
        ),
        migrations.AlterModelOptions(
            name='esp_productos',
            options={'verbose_name_plural': 'Productos'},
        ),
        migrations.DeleteModel(
            name='Esp_Ingenieria_servicios',
        ),
        migrations.AddField(
            model_name='esp_servicios',
            name='producto',
            field=models.OneToOneField(null=True, to='esp.Esp_productos'),
        ),
    ]
