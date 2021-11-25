from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CompanyConfig(AppConfig):
    name = 'birzum.apps.smallapps.company'
    verbose_name = _("Tashkilot malumotlari")