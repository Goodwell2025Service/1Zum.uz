from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from birzum.apps.products.models import Product


User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Buyurtma egasi"),
        related_name="orders",
        blank=True)
    
    first_name = models.CharField(_("Ism"), max_length=255)
    last_name = models.CharField(_("Familiya"), max_length=255)
    # manzil malumotlari
    region = models.CharField(_("Viloyat"), max_length=100)
    district = models.CharField(_("Tuman/Shahar"), max_length=100)
    street = models.CharField(_("Ko'cha"), max_length=55)
    house = models.CharField(_("Massiv, Daha, Kvarta, uy nomeri"), max_length=255)
    postcode = models.PositiveIntegerField(_("Pochta indexi"), blank=True)
    email = models.EmailField(_("E-pochta"), blank=True)
    phone = models.CharField(_("Telefon"), max_length=13)
    # xaridor tomonidan qo'shimcha xabar
    message = models.TextField(_("Qo'shimcha xabar"), blank=True)
    # to'lov turi
    payment = models.CharField(_("To'lov turi"), max_length=55, blank=True)
    # yetkazib berish
    shipping = models.CharField(_("Yetkazib berish"), max_length=55, blank=True)

    class Meta:
        verbose_name = _("buyurtma")
        verbose_name_plural = _("Buyurtmalar")

    def get_client_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.get_client_name()} - {self.district}, {self.district}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE, verbose_name=_("buyurtma"))
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name=_("Mahsulot"))
    price = models.DecimalField(_('narx'),max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(
        _('Soni'),default='1', validators=[MaxValueValidator(1000), MinValueValidator(1)])
    
    class Meta:
        verbose_name = _("buyurtma")
