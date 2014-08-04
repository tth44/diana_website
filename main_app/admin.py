from django.contrib import admin
from main_app.models import *
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js

# Register your models here.
class ContentInlines(admin.StackedInline):
    model = Content
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines =[ContentInlines]
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)