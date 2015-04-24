from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from wkhtmltopdf.views import PDFTemplateResponse

from .models import *

class IndexView(generic.View):

	def get(self, request, *args, **kwargs):
		return render(request,'page/index.html')

class BibliotecaView(generic.View):

	def get(self, request, *args, **kwargs):
		lista 		= Libro.objects.all()
		paginator 	= Paginator(lista, 10)
		page 		= request.GET.get('page')

		try:
			libros 	= paginator.page(page)
		except PageNotAnInteger:
			libros 	= paginator.page(1)
		except EmptyPage:
			libros 	= paginator.page(paginator.num_pages)

		return render(request,'page/biblioteca/biblioteca.html',{'libros':libros})

class HemerotecaView(generic.View):

	def get(self, request, *args, **kwargs):
		lista 		= Periodico.objects.all()
		paginator 	= Paginator(lista, 10)
		page 		= request.GET.get('page')

		try:
			periodicos = paginator.page(page)
		except PageNotAnInteger:
			periodicos = paginator.page(1)
		except EmptyPage:
			periodicos = paginator.page(paginator.num_pages)

		return render(request,'page/hemeroteca/hemeroteca.html',{'periodicos':periodicos})

class LibroCreate(generic.CreateView):
	model 			= Libro
	template_name 	= 'page/biblioteca/libro_form.html'
	fields 			= [	'codigo','autores','titulo','edicion','anio','contenido','fotoportada','ubicacion','estado',
						'clasificacion','descripcion','observaciones']
	success_url 	= reverse_lazy('page:biblioteca')

class PeriodicoCreate(generic.CreateView):
	model 			= Periodico
	template_name 	= 'page/hemeroteca/periodico_form.html'
	fields 			= [	'volumen','nombre','fecha_inicio','fecha_fin','estado','clasificacion','tipo_periodico',
						'ubicacion','descripcion','observaciones']
	success_url 	= reverse_lazy('page:hemeroteca')

class LibroUpdate(generic.UpdateView):
	model 			= Libro
	template_name 	= 'page/biblioteca/libro_form.html'
	fields 			= [	'codigo','autores','titulo','edicion','anio','contenido','fotoportada','ubicacion','estado',
						'clasificacion','descripcion','observaciones']
	success_url 	= reverse_lazy('page:biblioteca')

class PeriodicoUpdate(generic.UpdateView):
	model 			= Periodico
	template_name 	= 'page/hemeroteca/periodico_form.html'
	fields 			= [	'volumen','nombre','fecha_inicio','fecha_fin','estado','clasificacion','tipo_periodico',
						'ubicacion','descripcion','observaciones']
	success_url 	= reverse_lazy('page:hemeroteca')

class LibroDelete(generic.DeleteView):
	model 			= Libro
	template_name 	= 'page/biblioteca/libro_delete.html'
	success_url 	= reverse_lazy('page:libro_delete')

class PeriodicoDelete(generic.DeleteView):
	model 			= Periodico
	template_name 	= 'page/hemeroteca/periodico_delete.html'
	success_url 	= reverse_lazy('page:periodico_delete')

class LibroView(generic.TemplateView):

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		opcion = request.POST['opcion']
		if opcion == '1':
			libros = Libro.objects.filter(codigo__contains=buscar)
			contexto = {'libros':libros,'libro':True}
			return render(request,'page/biblioteca/libro_view.html',contexto)
		if opcion == '2':
			libros = Libro.objects.filter(autores__contains=buscar)
			contexto = {'libros':libros,'libro':True}
			return render(request,'page/biblioteca/libro_view.html',contexto)
		if opcion == '3':
			libros = Libro.objects.filter(titulo__contains=buscar)
			contexto = {'libros':libros,'libro':True}
			return render(request,'page/biblioteca/libro_view.html',contexto)
		else:
			return render(request,'page/biblioteca/libro_view.html')

class PeriodicoView(generic.TemplateView):

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		opcion = request.POST['opcion']
		if opcion == '1':
			periodicos = Periodico.objects.filter(volumen__contains=buscar)
			contexto = {'periodicos':periodicos,'periodico':True}
			return render(request,'page/hemeroteca/periodico_view.html',contexto)
		if opcion == '2':
			periodicos = Periodico.objects.filter(nombre__contains=buscar)
			contexto = {'periodicos':periodicos,'periodico':True}
			return render(request,'page/hemeroteca/periodico_view.html',contexto)
		else:
			return render(request,'page/hemeroteca/periodico_view.html')

class LibroSearch(generic.View):

	def get(self, request, *args, **kwargs):
		return render(request,'page/biblioteca/libro_search.html')

class PeriodicoSearch(generic.View):

	def get(self, request, *args, **kwargs):
		return render(request,'page/hemeroteca/periodico_search.html')

def to_pdf(request):
	libros = Libro.objects.all()
	return PDFTemplateResponse(request,'page/biblioteca/pdf.html',{'libros':libros})