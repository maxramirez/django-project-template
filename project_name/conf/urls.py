from django.conf.urls import patterns, url, include
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.views.defaults.page_not_found', name='index')
)
