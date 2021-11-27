from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class AboutUs(TimeStampedModel):
    # kirish bo'limi
    title = models.CharField(_("Sarlavha"), max_length=255)
    description = models.TextField(_("Tavsif"), blank=True)

    first_large_image = models.ImageField(_("Birinchi HD rasm"), blank=True)

    # xizmat turlari bo'limi
    show_features = models.BooleanField(_("Xizlat turlari haqida malumotni ko'rsatish"), default=True)
    first_feature = models.TextField(
        _("Birinchi xizmat turi"),
        help_text=_("Xaridorlarga xizmat ko'rsatish haqida"),
        max_length=512)
    second_feature = models.TextField(
        _("Uchinchi xizmat turi"),
        help_text=_("Onlayn qo'llab quvvatlash haqida"),
        max_length=512)
    third_feature = models.TextField(
        _("Ikkinchi xizmat turi"),
        help_text=_("Xarid bo'yicha konsultatsiya haqida"),
        max_length=512)

    feature_image = models.ImageField(_("Xizmat turlariga oid rasm"), blank=True)

    # qisqacha statistika bo'limi
    show_statistics = models.BooleanField(_("Statistika bo'limini ko'rsatish"), default=True)

    products_in_sale = models.IntegerField(_("Sotuvdagi productlar"), default=0, blank=True)
    products_in_sale_description = models.CharField(_("Sotuvdagi mahsulotlar tavsifi"), max_length=155, blank=True)

    community_earnings = models.DecimalField(_("Jamoa jamg'armasi"), max_digits=10, decimal_places=2, blank=True)
    community_earnings_description = models.CharField(_("Qisqacha tavsif"), blank=True, max_length=155)

    buyer_count = models.IntegerField(_("Xaridorlar soni"), default=0, blank=True)
    buyer_count_description = models.CharField(_("Xaridorlar haqida qisqacha tavsif"), max_length=155, blank=True)

    # xaridorlar hayoti haqida qaygurish bo'limi ^-^
    show_think_about_customers = models.BooleanField(_("Xaridorlar haqida qaygurish bo'limini ko'rsatish"), default=True)
    
    think_about_customers_image = models.ImageField(_("Xaridorlar haqida o'ylaymiz rasmi"), blank=True)
    think_about_customers_description = models.TextField(_("Qisqacha tavsif"), blank=True, max_length=512)

    class Meta:
        verbose_name = _("malumot")
        verbose_name_plural = _("Kompaniya haqida")

    def __str__(self):
        return f"# {self.id} - malumot"


class Contact(TimeStampedModel):
    title = models.CharField(_("Aloqa sarlavhasi"), blank=True, max_length=255)
    description = models.CharField(_("Qisqacha tavsif"), blank=True, max_length=255)

    email = models.EmailField(_("E.pochta"))
    phone = models.CharField(_("Telefon raqam"), max_length=13)
    adress = models.CharField(_("Manzil"), max_length=155)
    fax = models.CharField(_("Fax raqami"), max_length=15, blank=True)

    class Meta:
        verbose_name = _("malumot")
        verbose_name_plural = _("Kontaktlar")
    
    def __str__(self):
        return f"{self.id} Kontakt malumoti"


class Features(TimeStampedModel):
    title = models.CharField(_("Xususiyat nomi"), max_length=155)
    description = models.TextField(_("Qisqacha tavsif"), max_length=155)
    icon_class = models.CharField(_("Ikonka nomi"), max_length=55)

    class Meta:
        verbose_name = _("xususiyat")
        verbose_name_plural = _("Xususiyatlar")

    def __str__(self):
        return self.title


class Awards(TimeStampedModel):
    title = models.CharField(_("Yutuq nomi"), max_length=255)
    image = models.ImageField(_("Yutuq rasmi"))

    class Meta:
        verbose_name = _("yutuq")
        verbose_name_plural = _("Yutuqlar")

    def __str__(self):
        return self.title


class Leaders(TimeStampedModel):
    name = models.CharField(_("Xodimning ismi sharfi"), max_length=155)
    role = models.CharField(_("Lavozimi"), max_length=155)
    # social links
    facebook = models.CharField(_("Facebookdagi foydalanuvchi nomi"), blank=True, max_length=55)
    twitter = models.CharField(_("Twitterdagi foydalanuvchi nomi"), blank=True, max_length=55)
    instagram = models.CharField(_("Instagram foydalanuvchi nomi"), blank=True, max_length=55)
    telegram = models.CharField(_("Telegram foydalanuvchi nomi"), blank=True, max_length=55)
    # user foto
    photo = models.ImageField(_("Xodim rasmi"), blank=True)

    class Meta:
        verbose_name = _("xodim")
        verbose_name_plural = _("Xodimlar")

    def __str__(self):
        return self.name
