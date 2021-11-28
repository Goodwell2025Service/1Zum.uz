from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from django.urls import reverse

User = get_user_model()


class New(TimeStampedModel):
    title = models.CharField(_('Nomi'), max_length=200, db_index=True)
    slug = models.SlugField(_('slug'), max_length=200, db_index=True, blank=True)
    body = models.TextField(_('Tavsifi'), blank=True)
    image = models.ImageField(_('rasm'), default='default.apng', blank=True, null=True)
    news = models.BooleanField(_('Yangilik'), default=False)
    stock = models.BooleanField(_('Chegirma'), default=False)

    class Meta:
        verbose_name_plural = _('Yangiliklar')
        verbose_name = _('yangilik')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    


class Partner(TimeStampedModel):
    title = models.CharField(_('Nomi'), max_length=200, db_index=True)
    slug = models.SlugField(_('slug'), max_length=200, db_index=True, blank=True)
    icon = models.ImageField(_("Hamkor logosi"))
    site_url = models.URLField(_('Websayt urli'), max_length=255)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = _('Hamkorlar')
        verbose_name = _('hamkor')

    def __str__(self):
        return self.title


class Savollar(TimeStampedModel):
    question = models.CharField(_("Savol"), max_length=512)
    answer = models.CharField(_("Javob"), max_length=512)
    order = models.PositiveIntegerField(_("Tartib"), default=0)

    class Meta:
        ordering = ('order',)
        verbose_name = _("Savol")
        verbose_name_plural = _("Savollar")

    def __str__(self) -> str:
        return self.question[:100]
