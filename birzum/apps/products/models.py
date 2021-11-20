
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


User = get_user_model()


class Brand(models.Model):
    name = models.CharField(_("Brend nomi"), max_length=55)
    icon = models.ImageField(_("Brend ikonkasi"), upload_to="brendlar/", blank=True)

    class Meta:
        verbose_name = _("brend")
        verbose_name_plural = _("Brendlar")
    
    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(_("Category"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_("Brend"),
        related_name=_("categories")
        )
    logo = models.ImageField(_("Logo"), upload_to="logo_image/", blank=True, null=True)
    image = models.ImageField(_("Rasmi"), upload_to="cat_image/", blank=True, null=True)

    order = models.IntegerField(_("Tartib raqami"), default=10)

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = _("kategoriya")
        verbose_name_plural = _("Kategoriyalar")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:list_by_category', kwargs={"cat_slug": self.slug})


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name="Categoriya"
        )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        verbose_name=_("Brend"),
        blank=True, null=True,
        related_name="products"
        )
    title = models.CharField(_("Nomi"), max_length=255)
    slug = models.SlugField(_("Slag"), max_length=255, unique=True)
    description = models.TextField(_("Tafsif"), blank=True)

    specs = RichTextField(_("Xarakteristika"), blank=True)
    available = models.BooleanField("Sotuvda mavjud", default=True)
    bestseller = models.BooleanField("Eng ko'p sotiladigan mahsulot", default=False)
    new = models.BooleanField("Yangi", default=False)

    price = models.DecimalField(_("Narx"), max_digits=10, decimal_places=2, blank=True)
    discount_price = models.DecimalField(_("Chegirma narx"), max_digits=10, decimal_places=2, blank=True)
    credit_price = models.DecimalField(_("Kredit narx"), max_digits=10, decimal_places=2, blank=True)

    class Meta:
        verbose_name = _("mahsulot")
        verbose_name_plural = _("Mahsulotlar")

    def __str__(self):
        return self.name

    def get_first_image_url(self):
        return self.image.first().image.url

    def get_price(self):
        return self.price.get(product__id=self.id).price

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={"cat_slug": self.category.slug, "slug": self.slug})

    @property
    def available_for_credit(self):
        return True if self.credit_price else False

    @property
    def is_discount(self):
        return True if self.discount_price else False


class Price(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(_("Narx"), max_digits=10, decimal_places=2)
    changed_by = models.ForeignKey(User, related_name="my_prices", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("narx")
        verbose_name_plural = _("Narxlar")

    def __str__(self):
        return f"{self.product}: {self.price} ({self.changed_by})"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(_("Masulot rasmi"), upload_to="images/%Y/%m/%d/")

    class Meta:
        verbose_name = _("mahsulot rasmi")
        verbose_name_plural = _("Mahsulotlar rasmlari")

    def __str__(self):
        return "Rasm - " + str(self.image.path)



