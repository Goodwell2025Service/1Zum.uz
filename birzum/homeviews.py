from django.views.generic import TemplateView

from birzum.apps.smallapps.reklama.models import HomePageBanner
# from birzum.apps.products.models import Category, Product
class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['banners'] = HomePageBanner.objects.all()
        print(ctx['banners'])
        return ctx
