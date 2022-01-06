from django.contrib import admin, messages
from mptt.admin import MPTTModelAdmin
from django.utils.translation import gettext_lazy as _
from django.core.management import call_command

from .models import Brand, Category, Image, Price, Product


def sumdagi_narxlarni_yangilash(modeladmin, request, queryset):
    """mahsulot narxlarini sumga almashtirish"""
    try:
        call_command("write_price_in_sum")
        messages.add_message(request, messages.SUCCESS, "Mahsulotlarning sumdagi narxlari yangilandi!")
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Operatsiyani bajarishda xatolik: " + str(e))
    return


sumdagi_narxlarni_yangilash.short_description = "Mahsulotlarning sumdagi narxlarini yangilash."

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
    actions = [sumdagi_narxlarni_yangilash,]


    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}



# login page title
admin.site.site_header = _("1zum online do'koni")

# admin index page title
admin.site.index_title = _("SAYT BO'LIMLARI")

