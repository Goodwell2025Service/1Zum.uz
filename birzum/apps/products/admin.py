from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Brand, Category, Image, Price, Product

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    search_fields = ['name']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


class ImageAdminInline(admin.TabularInline):
    model = Image
    extra = 1


class PriceAdminInline(admin.TabularInline):
    model = Price
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields = ['title']
    inlines = [PriceAdminInline, ImageAdminInline]

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
