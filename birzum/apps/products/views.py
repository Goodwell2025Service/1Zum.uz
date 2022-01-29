from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django_filters.views import FilterView
from django.core.paginator import Paginator

from birzum.apps.smallapps.company.models import Features
from birzum.apps.smallapps.rating.models import Rating
from .models import Category, Product, Brand
from .filters import ProductFilter
from .last_seen import Last
# Create your views here.


class Home(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        last = Last(self.request)
        ctx['categories'] = Category.objects.select_related('parent')
        ctx['last_seen'] = Product.objects.filter(id__in=last.box.keys()).prefetch_related('images')
        return ctx


home_view = Home.as_view()


class ProductList(FilterView):
    queryset = Product.objects.select_related('category', 'brand', 'chegirma').prefetch_related('image', 'ratings')
    filterset_class = ProductFilter

    def get_queryset(self, **kwargs):
        cat_slug = self.kwargs.get('cat_slug', None)
        paginate = self.request.GET.get('paginate', 9)
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
        ctx['brands'] = Brand.objects.select_related('category').prefetch_related('product').all()
        ctx['cats'] = Category.objects.filter(image__isnull=False).select_related('parent')
        return ctx


product_list_view = ProductList.as_view()


class ProductDetail(DetailView):
    queryset = Product.objects.select_related(
        'category', 'brand', 'chegirma').prefetch_related('image', 'ratings').all()
    slug_field = 'slug'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = Category.objects.select_related('parent').all()
        return ctx

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["features"] = Features.objects.all()
        if self.object.brand:
            context["products_from_this_vendor"] = Product.items.in_same_vendor(
                brand_id=self.object.brand.id, prod_id=self.object.id)
        context["products_in_this_cat"] = Product.items.in_same_category(
            cat_id=self.object.category_id, prod_id=self.object.id)
        context["more"] = Product.items.more()
        context["comments"] = Rating.objects.select_related('product').filter(
            product=self.object, published=True)
        return context

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        last_seen = Last(self.request)
        last_seen.add(product_id=obj.id)
        return obj


product_detail_view = ProductDetail.as_view()
