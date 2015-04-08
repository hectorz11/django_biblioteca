from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings

urlpatterns = patterns('',

	url(r'^', include('page.urls', namespace='page')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
