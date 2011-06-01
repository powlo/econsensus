from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

import openconsent.publicweb.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', openconsent.publicweb.views.groups, name='groups'),
    url(r'^public/', include('openconsent.publicweb.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
    
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            { 'document_root' : settings.MEDIA_ROOT })
    )