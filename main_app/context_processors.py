'''
Created on 27 juil. 2014

@author: matthieu
'''

from main_app.models import Category
from portfolio.models import Project

def cats(context):
    
    return {'cats': Category.objects.all().order_by('position') }

def contactCat(context):
    
    return { 'contactCat' : Category.objects.filter(type = 'contact').first()}
    