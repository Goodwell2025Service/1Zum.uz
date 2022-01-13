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
    if request.path_info in ['/uz/', '/ru/']:
        categories = Category.objects.select_related('parent').exclude(hide=True)
    else:
        categories = Category.objects.select_related('parent').all()
    return {'categories': categories}
