from django.contrib import admin
from portfolio.models import *
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js

# Register your models here.

class ImagesForGalleryInline(admin.TabularInline):
    model = ImagesForGallery

     
         
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImagesForGalleryInline]
    prepopulated_fields = {'display_title': ('title',)}
    class Media:
        js= ('//tinymce.cachefly.net/4.1/tinymce.min.js','www/js/tiny_mce_textareas.js')

admin.site.register(Project, ProjectAdmin)


