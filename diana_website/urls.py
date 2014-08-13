from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diana_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^portfolio/', include("portfolio.urls")),
    url(r'^cv/', include("cv.urls")),
    url(r'^contact$', 'main_app.views.contact', name ='main_app_contact' ),
    url(r'^$', 'main_app.views.home', name='main_app_home'),
    url(r'^(?P<catSlug>([a-z]+\-*[a-z]+\-*)+)$', 'main_app.views.index', name='main_app_index'),
    
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
