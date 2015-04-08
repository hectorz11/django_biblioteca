# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_paginas', models.IntegerField(null=True, verbose_name=b'Numero de paginas', blank=True)),
                ('anio', models.CharField(max_length=20, null=True, blank=True)),
                ('numero_edicion', models.IntegerField(null=True, verbose_name=b'Numero de edicion', blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('foto', models.ImageField(null=True, upload_to=b'images/periodicos/', blank=True)),
                ('descripcion', models.TextField(max_length=1500, null=True, blank=True)),
                ('observaciones', models.TextField(max_length=450, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContenidoDigital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto_digital', models.ImageField(upload_to=b'images/digitales/', null=True, verbose_name=b'Foto Digital', blank=True)),
                ('descripcion', models.TextField(max_length=1500, null=True, blank=True)),
                ('contenido', models.ForeignKey(verbose_name=b'Periodico', to='page.Contenido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=15)),
                ('autores', models.CharField(max_length=250, null=True, verbose_name=b'Autor(es)', blank=True)),
                ('titulo', models.CharField(max_length=250, null=True, blank=True)),
                ('edicion', models.CharField(max_length=75, null=True, blank=True)),
                ('anio', models.CharField(max_length=20, null=True, blank=True)),
                ('contenido', models.TextField(max_length=1500, null=True, blank=True)),
                ('fotoportada', models.ImageField(upload_to=b'images/libros/', null=True, verbose_name=b'Foto de Portada', blank=True)),
                ('descripcion', models.TextField(max_length=1500, null=True, blank=True)),
                ('observaciones', models.TextField(max_length=450, null=True, blank=True)),
                ('clasificacion', models.ForeignKey(to='page.Clasificacion')),
                ('estado', models.ForeignKey(to='page.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volumen', models.IntegerField(null=True, blank=True)),
                ('nombre', models.CharField(max_length=250, null=True, blank=True)),
                ('fecha_inicio', models.DateField(null=True, verbose_name=b'Fecha de inicio', blank=True)),
                ('fecha_fin', models.DateField(null=True, verbose_name=b'Fecha de finalizacion', blank=True)),
                ('descripcion', models.TextField(max_length=1500, null=True, blank=True)),
                ('observaciones', models.TextField(max_length=450, null=True, blank=True)),
                ('clasificacion', models.ForeignKey(to='page.Clasificacion')),
                ('estado', models.ForeignKey(to='page.Estado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='periodico',
            name='tipo_periodico',
            field=models.ForeignKey(verbose_name=b'Tipo de Periodico', to='page.Tipo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='periodico',
            name='ubicacion',
            field=models.ForeignKey(to='page.Ubicacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='libro',
            name='ubicacion',
            field=models.ForeignKey(to='page.Ubicacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contenido',
            name='periodico',
            field=models.ForeignKey(to='page.Periodico'),
            preserve_default=True,
        ),
    ]
