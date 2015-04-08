from django.contrib import admin
from .models import *

class LibroAdmin(admin.ModelAdmin):
	list_display = ('id','codigo','autores','titulo','estado')
	search_fields = ['codigo','autores','titulo']
	list_filter = ('estado','clasificacion')

class PeriodicoAdmin(admin.ModelAdmin):
	list_display = ('id','volumen','nombre','fecha_inicio','fecha_fin','estado')
	search_fields = ['voumen','nombre']
	list_filter = ('estado','clasificacion')

admin.site.register(Estado)
admin.site.register(Clasificacion)
admin.site.register(Tipo)
admin.site.register(Ubicacion)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Periodico,PeriodicoAdmin)
admin.site.register(Contenido)
admin.site.register(ContenidoDigital)