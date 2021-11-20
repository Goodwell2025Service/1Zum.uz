from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrderConfig(AppConfig):
    name = 'birzum.apps.order'

    verbose_name = _("Buyurtmalar")