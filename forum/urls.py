from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from myforum import formurls
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'forum.views.home', name='home'),
                       # url(r'^forum/', include('forum.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       #    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^$', include(formurls)),
                       url(r'^admin/', include(admin.site.urls)),
                       )
