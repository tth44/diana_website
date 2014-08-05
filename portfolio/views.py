# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.http import HttpResponse
from models import *
from django.core.urlresolvers import reverse
from main_app.models import *
from pip._vendor.distlib._backport.tarfile import TUREAD
from django.core.exceptions import PermissionDenied

# Create your views here.

def index(request,catSlug):
    
    cat = get_object_or_404(Category.objects.filter(type="portfolio"),slug=catSlug)
    print cat.title
    projects = Project.objects.filter(cat=cat.id )
    
    projectsAndPicOnTop= {}
    for p in projects:
        projectsAndPicOnTop[p] = p.imagesforgallery_set.filter(onTop = True).first()

    print projectsAndPicOnTop
    return render(request, 'portofolio_index.html', { 'projectsAndPicOnTop':projectsAndPicOnTop, 'cat': cat})




def detailsProject(request, catSlug, projectSlug):
    
    print "projectslug: " + projectSlug
    p = get_object_or_404(Project, slug ="manifesto-urban-decay-to-infinite-recycling")
    print p.slug
    p = get_object_or_404(Project, slug=projectSlug)
    #if the project does not belong to the category
    print p
    if p.cat.slug != catSlug:
        raise Http404
    
    images = p.imagesforgallery_set.all()   
    return render(request, 'projects.html', {'project' : p, 'images': images})


def denied(request):
    raise PermissionDenied

#===============================================================================
# def redirectProject(request, catSlug, projectId):
#     
#     p = get_object_or_404(Project, pk=projectId)
#     if p.cat.slug != catSlug:
#         raise Http404
#     
#     return redirect(reverse('detailsProject', kwargs={'projectId':projectId, 'projectSlug': p.slug, 'catSlug': catSlug}), permanent=True)
#     
#===============================================================================
