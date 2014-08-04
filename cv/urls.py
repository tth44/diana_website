'''
Created on Jul 29, 2014

@author: mdesbois
'''
from django.conf.urls import patterns, url
from cv import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='cv_index'),
)