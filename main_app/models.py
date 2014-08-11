from django.db import models
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse 
# Create your models here.

class CategoryAbstract(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True)
    position = models.IntegerField(help_text="Position in the menu")
    class Meta:
        app_label = "main_app"
        abstract = True
        ordering = ['position']


class ContentAbstract(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True)
    description = models.TextField()
   
    class Meta:
        app_label = "main_app"
        abstract = True
  
  
    
class Category(CategoryAbstract):
    HOME = "home"
    PORTFOLIO = "portfolio"
    CV = "cv"
    CONTACT = "contact"
    
    ALLOWED_TYPES = (
                (HOME, "Home"),
                (PORTFOLIO, "Portfolio"),
                (CV , "CV"),
                (CONTACT, "Contact")
    )
    
    type = models.CharField(max_length=20, blank=True, choices=ALLOWED_TYPES, help_text="Indicate the type of category")
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        if self.type == self.PORTFOLIO:                                  
            return reverse('portfolio_index', kwargs={'catSlug' :self.slug})
        
        elif self.type == self.CV:
            return reverse('cv_index')
        
        elif self.type == self.HOME:
            return reverse('main_app_home')
        
        elif self.type == self.CONTACT:
            return reverse('main_app_contact')
        
        else:
            return reverse('main_app_home')
    
    class Meta:
        app_label = "main_app"
        


class Content(ContentAbstract):
    
    cat = models.ForeignKey('Category')
    def __unicode__(self):
        return self.title
    class Meta:
        app_label = "main_app"
        


#===============================================================================
# class Contact(models.Model):
#     
#     email = models.EmailField(primary_key=True)
#     name = models.CharField(max_length=100)
#   
#     
#     def __unicode__(self):
#         return self.name
#     class Meta:
#         app_label = "main_app"
#===============================================================================
