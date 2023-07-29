from django.contrib import admin
from .models import Property, Category, Viewing, About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Property)
class PropertyAdmin(SummernoteModelAdmin):
    
    list_display = ('name', 'price', 'property_type', 'category',)
    search_fields = ['category', 'property_type']
    list_filter = ('category', 'price', 'property_type',)
    summernote_fields = ('description',)
 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)

admin.site.register(Viewing)
admin.site.register(About)