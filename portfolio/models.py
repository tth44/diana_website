from django.db import models
import os
from autoslug import AutoSlugField
import main_app
from django.core.urlresolvers import reverse

# Create your models here.

        
        
class Project(main_app.models.ContentAbstract):
    
    cat = models.ForeignKey(main_app.models.Category)
    display_title = models.CharField(max_length = 50, help_text = "Title that you will see in the menu")
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('portfolio_detailsProject', kwargs={'catSlug' :self.cat.slug, 'projectSlug': self.slug})
    
    class Meta:
        app_label= "portfolio"
        
    
 
 
class ImagesForGallery(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100, blank = True)
    
    onTop = models.BooleanField(default=False)
    project = models.ForeignKey(Project)
    
    mini = models.ImageField(upload_to="mini") 
    medium = models.ImageField(upload_to="medium")
    full = models.ImageField(upload_to="full") 
    
    def __unicode__(self):
        return self.title
   
    class Meta:
        app_label= "portfolio"

