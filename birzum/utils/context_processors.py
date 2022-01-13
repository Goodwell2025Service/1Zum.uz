from django.conf import settings

from birzum.apps.products.models import Category
from birzum.apps.cart.cart import Cart


def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {"DEBUG": settings.DEBUG}

def local_context(request):
    categories = Category.objects.select_related('parent')[:8]
    return {'categories': categories}
