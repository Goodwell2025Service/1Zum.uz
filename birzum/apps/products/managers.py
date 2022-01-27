
from django.db import models


class ProductsManager(models.Manager):

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.prefetch_related('image', 'ratings').select_related('category', 'brand').all()
        return qs
    
    def get_next(self, id):
        return self.filter(id__gt=id).first()
    
    def get_prev(self, id):
        return self.filter(id__lt=id).first()

    def more(self):
        return self.get_queryset()[:6]

    def in_same_category(self, cat_id, prod_id):
        return self.get_queryset().filter(category=cat_id).exclude(id=prod_id)[:3]
    
    def in_same_vendor(self, brand_id, prod_id):
        return self.get_queryset().filter(brand=brand_id).exclude(id=prod_id)[:3]