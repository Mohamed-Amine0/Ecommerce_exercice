from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'featured', 'created_at')
    list_filter = ('category', 'featured', 'created_at')
    list_editable = ('featured',)
    search_fields = ('name', 'description')
    autocomplete_fields = ['category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
