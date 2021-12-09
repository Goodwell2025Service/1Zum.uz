from django.views.generic import TemplateView
from birzum.apps.products.models import Category, Product
from birzum.apps.blog.models import Partner
from birzum.apps.smallapps.company.models import Features


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['features'] = Features.objects.all()
        ctx['chegirmalar'] = 'something'
        ctx['day_hot_sale'] = 'something'
        ctx['week_hot_sale'] = 'something'
        ctx['hot_categories'] = 'something'
        ctx['hot_electronics'] = Product.objects.filter(category=2, available=True)[:8]
        ctx['hot_clothes'] = Product.objects.filter(category=3, available=True)[:8]
        ctx['top_rated'] = 'something'
        ctx['in_sale'] = 'something'
        ctx['bestsellers'] = Product.objects.filter(bestseller=True, available=True)[:3]
        ctx['latest'] = Product.objects.all().order_by('-created')[:3]
        ctx['partners'] = Partner.objects.exclude(icon__isnull=True).all()
        ctx['latest_news'] = 'something'
        ctx['recently_viewed'] = 'something'
        return ctx
