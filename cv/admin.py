from django.contrib import admin
from cv.models import *

# Register your models here.

class CVItemInlines(admin.StackedInline):
    model = CVItem
    extra = 1

class SubCVCategoryAdmin(admin.ModelAdmin):
    inlines = [CVItemInlines]
    prepopulated_fields = {'display_title': ('title',)}
    class Media:
        js= ('//tinymce.cachefly.net/4.1/tinymce.min.js','www/js/tiny_mce_textareas.js')
    
    
admin.site.register(SubCVCategory, SubCVCategoryAdmin)
