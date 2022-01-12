from modeltranslation.translator import register, TranslationOptions

from .models import HomePageBanner, HorizontalAdvert, HalfPageAdvert, SidebarAdvert, TopProductsAdvert


@register(HomePageBanner)
class HomePageBannerTranslationOptions(TranslationOptions):
    fields = ('banner_type', 'banner_cat_text', 'banner_info',)


@register(HorizontalAdvert)
class HorizontalAdvertTranslationOptions(TranslationOptions):
    fields = ('ad_title', 'ad_info',)


@register(HalfPageAdvert)
class HalfPageAdvertTranslationOptions(TranslationOptions):
    fields = ('ad_type', 'ad_title', 'ad_info',)


@register(SidebarAdvert)
class SidebarAdvertTranslationOptions(TranslationOptions):
    fields = ('ad_type', 'ad_title', 'ad_info',)


@register(TopProductsAdvert)
class TopProductsAdvertTranslationOptions(TranslationOptions):
    fields = ('ad_type', 'ad_title', 'ad_info',)

