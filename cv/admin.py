from django.contrib import admin
from cv.models import *

# Register your models here.

class CVItemInlines(admin.StackedInline):
    model = CVItem
    extra = 1

class SubCVCategoryAdmin(admin.ModelAdmin):
    inlines = [CVItemInlines]
    prepopulated_fields = {'display_title': ('title',)}
    
    
admin.site.register(SubCVCategory, SubCVCategoryAdmin)
