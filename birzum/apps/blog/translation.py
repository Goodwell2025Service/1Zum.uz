from modeltranslation.translator import register, TranslationOptions

from .models import New, Partner, Savollar


@register(New)
class NewTranslationOptions(TranslationOptions):
    fields = ('title', 'body',)


@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Savollar)
class SavollarTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)
