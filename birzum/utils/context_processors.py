from django.conf import settings
from birzum.apps.products.models import Category


def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {"DEBUG": settings.DEBUG}

def categories(request):
    categories = Category.objects.select_related('parent').all()
    return {'categories': categories}
