# -*- coding: utf-8 -*-

from django.shortcuts import *
from django.http import HttpResponse
from models import *
from django.core.urlresolvers import reverse


def index(request):
    
    sub = SubCVCategory.objects.all()
    
    return render(request,'cv.html',{'sub': sub})