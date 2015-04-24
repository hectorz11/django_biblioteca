from django.conf.urls import patterns, url
from page import views

urlpatterns = patterns('',

	# Vista
	url(r'^$', views.IndexView.as_view(), name='index'),

	# Listas - List
	url(r'biblioteca/$', views.BibliotecaView.as_view(), name='biblioteca'),
	url(r'hemeroteca/$', views.HemerotecaView.as_view(), name='hemeroteca'),

	# Crear - Create
	url(r'libro/create/$', views.LibroCreate.as_view(), name='libro_create'),
	url(r'periodico/create/$', views.PeriodicoCreate.as_view(), name='periodico_create'),

	# Actualizar - Update
	url(r'libro/update/(?P<pk>\d+)/$', views.LibroUpdate.as_view(), name='libro_update'),
	url(r'periodico/update/(?P<pk>\d+)/$', views.PeriodicoUpdate.as_view(), name='periodico_update'),

	# Eliminar - Delete
	url(r'libro/delete/(?P<pk>\d+)/$', views.LibroDelete.as_view(), name='libro_delete'),
	url(r'periodico/delete/(?P<pk>\d+)/$', views.PeriodicoDelete.as_view(), name='periodico_delete'),

	url(r'libro/search/$', views.LibroSearch.as_view(), name='libro_search'),
	url(r'libro/view/$', views.LibroView.as_view(), name='libro_view'),
	url(r'periodico/search/$', views.PeriodicoSearch.as_view(), name='periodico_search'),
	url(r'periodico/view/$', views.PeriodicoView.as_view(), name='periodico_view'),

	url(r'^topdf/$', views.to_pdf, name='to_pdf'),
)