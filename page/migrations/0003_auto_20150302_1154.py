# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20150302_1153'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Abicacion',
            new_name='Ubicacion',
        ),
    ]
