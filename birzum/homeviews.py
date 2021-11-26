from django.views.generic import TemplateView

# from birzum.apps.products.models import Category, Product
class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['features'] = 'something'
        ctx['chegirmalar'] = 'something'
        ctx['day_hot_sale'] = 'something'
        ctx['week_hot_sale'] = 'something'
        ctx['hot_categories'] = 'something'
        ctx['hot_electronics'] = 'something'
        ctx['hot_clothes'] = 'something'
        ctx['bestsellers'] = 'something'
        ctx['top_rated'] = 'something'
        ctx['in_sale'] = 'something'
        ctx['latest'] = 'something'
        ctx['partners'] = 'something'
        ctx['latest_news'] = 'something'
        ctx['recently_viewed'] = 'something'
        return ctx
