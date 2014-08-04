'''
Created on Jul 25, 2014

@author: mdesbois
'''
from django.conf.urls import patterns, url
from portfolio import views

urlpatterns = patterns('',
    url(r'^(?P<catSlug>[a-z]+\-*[a-z]+)$', views.index, name='portfolio_index'),
    url(r'^(?P<catSlug>[a-z]+\-*[a-z]+)/(?P<projectSlug>[a-z]+\-*[a-z]+)', views.detailsProject, name ='portfolio_detailsProject'),
    url(r'^$', views.denied)                 
    #url(r'^(?P<catSlug>[a-z]+\-*[a-z]+)/(?P<projectId>[0-9]+)', views.redirectProject)
)