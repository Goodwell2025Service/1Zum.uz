from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django_filters.views import FilterView

from birzum.apps.smallapps.company.models import Features
from .models import Category, Product, Brand
from .filters import ProductFilter
# Create your views here.


class Home(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.select_related('parent').all()
        return ctx


home_view = Home.as_view()


class ProductList(FilterView):
    queryset = Product.objects.select_related('category', 'brand').prefetch_related('image').all()
    filterset_class = ProductFilter

    def get_queryset(self, **kwargs):
        cat_slug = self.kwargs.get('cat_slug', None)
        paginate = self.request.GET.get('paginate', 1)
        self.paginate_by = paginate
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
        ctx['brands'] = Brand.objects.all()
        return ctx


product_list_view = ProductList.as_view()


class ProductDetail(DetailView):
    model = Product
    slug_field = 'slug'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.select_related('parent').all()
        return ctx

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["features"] = Features.objects.all()
        context["products_from_this_vendor"] = Product.objects.filter(
            brand=self.object.brand).exclude(id=self.object.id)[:3]
        context["products_in_this_cat"] = Product.objects.filter(
            category=self.object.category).exclude(id=self.object.id)[:3]
        context["more"] = Product.objects.all().order_by('title')[:6]
        return context
    

product_detail_view = ProductDetail.as_view()
