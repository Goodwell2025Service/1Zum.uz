from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from birzum.apps.products.models import Product
# Create your models here.

User = get_user_model()


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='ratings')
    rate = models.IntegerField("Baho", default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Foydalanuvchi")
    person = models.CharField("Xaridor", max_length=55, blank=True)
    contact = models.CharField("Kontakti", max_length=13, blank=True)
    comment = models.TextField("Fikr", blank=True)
    published = models.BooleanField("Nashr qilindi", default=False)
    created = models.DateTimeField("qo'shildi", default=timezone.now)

    class Meta:
        verbose_name = _("reyting")
        verbose_name_plural = _("Reyting")

    def __str__(self) -> str:
        return "# " + str(self.pk)


class Currency(models.Model):
    updated = models.DateTimeField(_('Yangilandi'), auto_now_add=True, editable=False)
    currency = models.DecimalField(_('USD Reytingi'), max_digits=13, decimal_places=2, blank=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name = _('kurs')
        verbose_name_plural = _('Dollar kursi')
    
    def __str__(self):
        return f"{self.currency}"
