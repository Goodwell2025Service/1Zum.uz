from django.views.generic import DetailView, ListView, TemplateView

from .models import Category, Product

# Create your views here.


class Home(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.select_related('parent').all()
        return ctx


home_view = Home.as_view()


class ProductList(ListView):
    queryset = Product.objects.prefetch_related('image').all()

    def get_queryset(self, **kwargs):
        try:
            return self.queryset.filter(category__slug=self.kwargs['cat_slug'])
        except Exception as e:
            print("Did not filter by category because %s" % e)
            return self.queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.select_related('parent').all()
        return ctx


product_list_view = ProductList.as_view()


class ProductDetail(DetailView):
    model = Product
    # pk_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.select_related('parent').all()
        return ctx


product_detail_view = ProductDetail.as_view()
