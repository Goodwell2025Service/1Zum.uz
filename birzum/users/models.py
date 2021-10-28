from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class GenderChoices(models.IntegerChoices):
    HIDDEN = 1, _("Hidden")
    MALE = 2, _("Male")
    FEMALE = 3, _("Female")


class User(AbstractUser):

    """Default user for birZum ecommerce system."""

    phone = models.CharField(_("Телефон"), max_length=50, blank=True, null=True)
    birth_date = models.DateField(_("Birth date"), blank=True)
    gender = models.CharField(
        _("Gender"), 
        choices=GenderChoices.choices, 
        default=GenderChoices.HIDDEN,
        max_length=55)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        # return reverse("users:detail", kwargs={"pk": self.pk})
        pass

    def get_full_name(self):
        """
        Return first and last names if user is individual, organization_name otherwise
        """
        return f"{self.first_name} {self.last_name}"
