from django.contrib import admin

from .models import HomePageBanner, TopProductsAdvert, SidebarAdvert, HalfPageAdvert, HorizontalAdvert

@admin.register(HomePageBanner)
class BannerAdmin(admin.ModelAdmin):
    pass


admin.site.register(TopProductsAdvert)
admin.site.register(HorizontalAdvert)
admin.site.register(SidebarAdvert)
admin.site.register(HalfPageAdvert)
