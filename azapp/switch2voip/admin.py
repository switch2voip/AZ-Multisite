from django.contrib import admin
from .models import Category, Product, ProductTag, ProductPicture, Variant


class ProductTagInline(admin.TabularInline):
    model = ProductTag
    fields = ['tag',]

class ProductPictureInline(admin.TabularInline):
    model = ProductPicture
    fields = ['picture',]


class ProductVariantInline(admin.TabularInline):
    model = Variant
    fields = ['name', 'price']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductTagInline,ProductVariantInline,ProductPictureInline]
    list_display = ['name', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'category', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
    ordering = ['-updated_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','created_at','updated_at']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']

# @admin.register(Variant)
# class VariantAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']

#
# from django.contrib.sites.models import Site
# admin.site.unregister(Site)
# class SiteAdmin(admin.ModelAdmin):
#     fields = ('id', 'name', 'domain')
#     readonly_fields = ('id',)
#     list_display = ('id', 'name', 'domain')
#     list_display_links = ('name',)
#     search_fields = ('name', 'domain')
# admin.site.register(Site, SiteAdmin)
