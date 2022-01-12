from modeltranslation.translator import register, TranslationOptions

from .models import AboutUs, Contact, Features, Awards, Leaders


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'first_feature', 'second_feature', 'third_feature',
                'products_in_sale_description', 'community_earnings_description', 'buyer_count_description',
                'think_about_customers_description',)


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'adress')


@register(Features)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Awards)
class AwardsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Leaders)
class LeadersTranslationOptions(TranslationOptions):
    fields = ('name', 'role',)
