from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from birzum.apps.smallapps.company.models import Features
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
        cat_slug = self.kwargs.get('cat_slug', None)
        print("cat_slug", cat_slug)
        if cat_slug:
            categories = get_object_or_404(Category, slug=cat_slug)
        try:
            return self.queryset.filter(
                category__in=categories.get_descendants(include_self=True)
                )
        except Exception as e:
            return self.queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.select_related('parent').all()
        return ctx


product_list_view = ProductList.as_view()


class ProductDetail(DetailView):
    model = Product
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["features"] = Features.objects.all()
        return context
    


product_detail_view = ProductDetail.as_view()
