
from django.db import models


class ProductsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()
    
    def get_next(self, id):
        return self.filter(id__gt=id).first()
    
    def get_prev(self, id):
        return self.filter(id__lt=id).first()

