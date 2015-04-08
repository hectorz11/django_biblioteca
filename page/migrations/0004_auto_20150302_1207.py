# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20150302_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='fecha',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodico',
            name='fecha_fin',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha de finalizacion', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodico',
            name='fecha_inicio',
            field=models.DateTimeField(null=True, verbose_name=b'Fecha de inicio', blank=True),
            preserve_default=True,
        ),
    ]
