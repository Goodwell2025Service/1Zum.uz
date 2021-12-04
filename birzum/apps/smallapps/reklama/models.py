from django.db import models
from django.utils.translation import gettext_lazy as _

from birzum.apps.products.models import Category


class HomePageBanner(models.Model):
    banner_type = models.CharField(_("Banner turi"), max_length=155)
    banner_cat_model = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Kategoriya"))
    banner_cat_text = models.CharField(_("Banner Kategoriyasi"), max_length=155, blank=True)
    banner_info = models.CharField(_("Qisqacha tavsif"), max_length=255, blank=True)
    button_link = models.URLField(_("Banner tugmasi uchun havola"), max_length=255, blank=True)
    banner_image = models.ImageField(_("Banner katta rasmi"), upload_to="banners", help_text="rezmer: 1903x520")
    banner_image_small = models.ImageField(_("Banner kichik rasmi"), upload_to="banners", help_text="rezmer: 70x70")

    class Meta:
        verbose_name = _("banner")
        verbose_name_plural = _("Bosh sahifa bannerlari")
    
    def __str__(self):
        return self.banner_type


class HorizontalAdvert(models.Model):
    ad_discount = models.CharField(_("Chegirma miqdori (%)"), max_length=10)
    ad_title = models.CharField(_("Sarlavha"), max_length=55)
    ad_info = models.CharField(_("Qisqa tavsif"), max_length=55)
    button_link = models.URLField(_("Reklama havolasi"), max_length=255)
    banner = models.ImageField(_("Reklama banneri"), upload_to="banners", help_text="razmer: 1240x198")

    class Meta:
        verbose_name = _("malumot")
        verbose_name_plural = _("Gorizontal uzun reklama banneri")
    
    def __str__(self):
        return self.ad_title


class HalfPageAdvert(models.Model):
    ad_type = models.CharField(_("Reklama turi"), max_length=55)
    ad_title = models.CharField(_("Sarlavha"), max_length=55)
    ad_info = models.CharField(_("Qisqa tavsif"), max_length=55)
    button_link = models.URLField(_("Reklama hovolasi"), max_length=255)
    banner = models.ImageField(_("Reklama banneri"), upload_to="banners", help_text="razmer: 610x200")

    class Meta:
        verbose_name = _("malumot")
        verbose_name_plural = _("Sahifa yarmini oluvchi reklama banneri")
    
    def __str__(self):
        return self.ad_title


class SidebarAdvert(models.Model):
    ad_type = models.CharField(_("Reklama turi"), max_length=55)
    ad_title = models.CharField(_("Sarlavha"), max_length=55)
    ad_info = models.CharField(_("Qisqa tavsif"), max_length=55)
    button_link = models.URLField(_("Reklama hovolasi"), max_length=255)
    banner = models.ImageField(_("Reklama banneri"), upload_to="banners", help_text="razmer: 266x220")

    class Meta:
        verbose_name = _("malumot")
        verbose_name_plural = _("Mahsulotlar bo'limida o'ng yondagi kichik reklama banneri")
    
    def __str__(self):
        return self.ad_title


class TopProductsAdvert(models.Model):
    ad_type = models.CharField(_("Reklama turi"), max_length=55)
    ad_title = models.CharField(_("Sarlavha"), max_length=55)
    ad_info = models.CharField(_("Qisqa tavsif"), max_length=55)
    button_link = models.URLField(_("Reklama hovolasi"), max_length=255)
    banner = models.ImageField(_("Reklama banneri"), upload_to="banners", help_text="razmer: 395x675")

    class Meta:
        verbose_name = _("malumot")
        verbose_name_plural = _("Mahsus malumotlari bo'limi [chapdagi uzun vertikal reklama]")
    
    def __str__(self):
        return self.ad_title
