from django.conf import settings
from django.urls import reverse

from birzum.apps.products.models import Category
from birzum.apps.cart.cart import Cart


def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {"DEBUG": settings.DEBUG}

def local_context(request):
    cats = Category.objects.filter(hide=False).select_related('parent')
    return {'categories': cats}
