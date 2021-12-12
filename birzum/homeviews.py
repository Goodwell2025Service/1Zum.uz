from django.views.generic import TemplateView

from birzum.apps.products.models import Product
from birzum.apps.smallapps.reklama.models import HomePageBanner
from birzum.apps.smallapps.company.models import Features
from birzum.apps.blog.models import Partner, New
# from birzum.apps.products.models import Category, Product
class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['banners'] = HomePageBanner.objects.all()
        ctx['features'] = Features.objects.all()
        ctx['partners'] = Partner.objects.all()
        ctx['last'] = Product.objects.all().order_by('created')[:4]
        ctx['products'] = Product.objects.all()[:3]
        ctx['bestseller'] = Product.objects.filter(bestseller=True)[:3]
        ctx['best'] = Product.objects.all()[:3]
        ctx['posts'] = New.objects.all().order_by('created')
        return ctx
