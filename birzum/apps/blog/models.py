from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel

User = get_user_model()


class New(TimeStampedModel):
    title = models.CharField(_('Nomi'),max_length=200, db_index=True)
    slug = models.SlugField(_('slug'), max_length=200, db_index=True, blank=True)
    body = models.TextField(_('Tavsifi'), blank=True)
    image = models.ImageField(_('rasm'),size=[300, 300], default='default.apng', blank=True, null=True)
    news = models.BooleanField(_('Yangilik'), default=False)
    stock = models.BooleanField(_('Chegirma'), default=False)
    
    class Meta:
        verbose_name_plural = _('Posts')
        verbose_name = _('post')

    def __str__(self) -> str:
        return self.title


class Partner(TimeStampedModel):
    title = models.CharField(_('Nomi'), max_length=200, db_index=True)
    slug = models.SlugField(_('slug'),max_length=200, db_index=True, blank=True)
    icon = models.ImageField(_("Hamkor logosi"))
    site_url = models.URLField(_('Websayt urli'), max_length=255)

    class Meta:
        ordering = ('-published',)
        verbose_name_plural = _('Partners')

    def __str__(self):
        return self.title


class Savollar(TimeStampedModel):
    question = models.CharField(_("Savol"), max_length=512)
    answer = models.CharField(_("Javob"), max_length=512)
    order = models.PositiveIntegerField(_("Tartib"), default=0, max_length=10)

    class Meta:
        ordering = ('order',)
        verbose_name = _("Savol")
        verbose_name_plural = _("Savollar")

    def __str__(self) -> str:
        return self.question[:100]
