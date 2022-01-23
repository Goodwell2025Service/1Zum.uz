from django.views.generic import TemplateView

from birzum.apps.products.models import Product
from birzum.apps.products.last_seen import Last
from birzum.apps.smallapps.reklama.models import *
from birzum.apps.smallapps.company.models import Features
from birzum.apps.blog.models import Partner, New
# from birzum.apps.products.models import Category, Product
class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        last = Last(self.request)
        ctx['last_seen'] = Product.objects.filter(
            id__in=last.box.keys()).select_related('brand', 'category').prefetch_related('image')
        ctx['banners'] = HomePageBanner.objects.all()
        ctx['big_vertical'] = HorizontalAdvert.objects.last()
        ctx['half_page'] = HalfPageAdvert.objects.all()[:2]
        ctx['right_side'] = SidebarAdvert.objects.last()
        ctx['top_prods'] = TopProductsAdvert.objects.last()
        ctx['features'] = Features.objects.all()
        ctx['partners'] = Partner.objects.all()
        ctx['products'] = Product.objects.select_related(
            'brand', 'category').prefetch_related('image')[:8]
        ctx['bestseller'] = Product.objects.filter(
            bestseller=True).select_related('brand', 'category').prefetch_related('image')[:3]
        ctx['posts'] = New.objects.all().order_by('created')
        return ctx
