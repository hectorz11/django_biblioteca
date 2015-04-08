from django.db import models

class Estado(models.Model):
	nombre = models.CharField(max_length=70)

	def __unicode__(self):
		return self.nombre

class Clasificacion(models.Model):
	nombre = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombre

class Ubicacion(models.Model):
	nombre = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nombre

class Tipo(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Libro(models.Model):

	def url(self,filename):
		ruta = "Libro/%s/%s"%(self.id,str(filename))
		return ruta

	codigo = models.CharField(max_length=15)
	autores = models.CharField(max_length=250,blank=True,null=True,verbose_name='Autor(es)')
	titulo = models.CharField(max_length=250,blank=True,null=True)
	edicion = models.CharField(max_length=75,blank=True,null=True)
	anio = models.CharField(max_length=20,blank=True,null=True)
	contenido = models.TextField(max_length=1500,blank=True,null=True)
	fotoportada = models.ImageField(upload_to=url,blank=True,null=True,verbose_name='Foto de Portada')
	ubicacion = models.ForeignKey(Ubicacion)
	estado = models.ForeignKey(Estado)
	clasificacion = models.ForeignKey(Clasificacion)
	descripcion = models.TextField(max_length=1500,blank=True,null=True)
	observaciones = models.TextField(max_length=450,blank=True,null=True)

	def __unicode__(self):
		return self.titulo

	class Meta:
		ordering = ['id']

class Periodico(models.Model):
	volumen = models.IntegerField(blank=True,null=True)
	nombre = models.CharField(max_length=250,blank=True,null=True)
	fecha_inicio = models.DateTimeField(auto_now=False,blank=True,null=True,verbose_name='Fecha de inicio')
	fecha_fin = models.DateTimeField(auto_now=False,blank=True,null=True,verbose_name='Fecha de finalizacion')
	estado = models.ForeignKey(Estado)
	clasificacion = models.ForeignKey(Clasificacion)
	tipo_periodico = models.ForeignKey(Tipo,verbose_name='Tipo de Periodico')
	ubicacion = models.ForeignKey(Ubicacion)
	descripcion = models.TextField(max_length=1500,blank=True,null=True)
	observaciones = models.TextField(max_length=450,blank=True,null=True)

	def __unicode__(self):
		return self.nombre

	class Meta:
		ordering = ['id']

class Contenido(models.Model):
	periodico = models.ForeignKey(Periodico)
	numero_paginas = models.IntegerField(blank=True,null=True,verbose_name='Numero de paginas')
	anio = models.CharField(max_length=20,blank=True,null=True)
	numero_edicion = models.IntegerField(blank=True,null=True,verbose_name='Numero de edicion')
	fecha = models.DateTimeField(auto_now=False,blank=True,null=True)
	foto = models.ImageField(upload_to='images/periodicos/',blank=True,null=True)
	descripcion = models.TextField(max_length=1500,blank=True,null=True)
	observaciones = models.TextField(max_length=450,blank=True,null=True)

	def __unicode__(self):
		return self.periodico.nombre

class ContenidoDigital(models.Model):
	foto_digital = models.ImageField(upload_to='images/digitales/',blank=True,null=True,verbose_name='Foto Digital')
	contenido = models.ForeignKey(Contenido,verbose_name='Periodico')
	descripcion = models.TextField(max_length=1500,blank=True,null=True)