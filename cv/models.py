from django.db import models
from autoslug import AutoSlugField
import main_app
from django.core.urlresolvers import reverse
# Create your models here.

class SubCVCategory(main_app.models.CategoryAbstract):
    
    description = models.TextField(blank = True)
    category = models.ForeignKey('main_app.Category')
    display_title = models.CharField(max_length = 50, help_text = "Title that you will see in the menu")
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "#" + self.slug
    
    
    class Meta:
        app_label= "cv"
        
    
class CVItem(main_app.models.ContentAbstract):
    
    category = models.ForeignKey('SubCVCategory')
    position = models.IntegerField(help_text = "Position in the menu")
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        app_label= "cv"
        ordering = ['position']