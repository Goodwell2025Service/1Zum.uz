from django.views.generic import TemplateView
from birzum.apps.products.models import Category, Product

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['features'] = 'something'
        ctx['chegirmalar'] = 'something'
        ctx['day_hot_sale'] = 'something'
        ctx['week_hot_sale'] = 'something'
        ctx['hot_categories'] = 'something'
        ctx['hot_electronics'] = Product.objects.filter(category=2)[:8]
        ctx['hot_clothes'] = Product.objects.filter(category=3)[:8]
        ctx['top_rated'] = 'something'
        ctx['in_sale'] = 'something'
        ctx['bestsellers'] = Product.objects.filter(bestseller=True, available=True)
        ctx['latest'] = Product.objects.all().order_by('-created')[:3]
        ctx['partners'] = 'something'
        ctx['latest_news'] = 'something'
        ctx['recently_viewed'] = 'something'
        return ctx
