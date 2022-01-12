from modeltranslation.translator import register, TranslationOptions

from .models import Product, Category, Chegirma


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'specs')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Chegirma)
class ChegirmaTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
