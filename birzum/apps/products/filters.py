import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Product, Category, Brand


class ProductFilter(django_filters.FilterSet):

    category = django_filters.MultipleChoiceFilter(
        field_name='category',
        choices=Category.objects.filter(level=0).values_list('id', 'name'),
        widget=forms.CheckboxSelectMultiple,
        method='category_filter',
    )

    brand = django_filters.MultipleChoiceFilter(
        field_name='brand',
        choices=Brand.objects.all().values_list('id', 'name'),
        widget=forms.CheckboxSelectMultiple,
        method='brand_filter',
    )

    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ["discount", "lising"]

    def category_filter(self, queryset, name, value):
        categories = Category.objects.filter(id__in=value).values_list('id')
        return queryset.filter(category__in=categories)

    def brand_filter(self, queryset, name, value):
        brands = Brand.objects.filter(id__in=value).values_list('id')
        return queryset.filter(brand__in=brands)

    def get_selected_discount(self):
        if not self.data:
            return False
        return self.data.get('discount')

    def get_selected_lising(self):
        if not self.data:
            return False
        return self.data.get('lising')

    def get_selected_min_price(self):
        if not self.data:
            return 0
        return self.data.get('min_price')

    def get_selected_max_price(self):
        if not self.data:
            return 0
        return self.data.get('max_price')
