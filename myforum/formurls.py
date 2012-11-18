# encoding:utf-8

from django.conf.urls import url, patterns


urlpatterns = patterns('',
           url(r'^$', 'myforum.views.main'),
#                       url(r'^thread/(\d+)/$', 'myforum.views.thread'),

#                       url(r'^forum/(\d+)/$', 'myforum.views.forum'),
                       )
