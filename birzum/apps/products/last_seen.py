from decimal import Decimal
from django.conf import settings
from .models import Product
from django.shortcuts import HttpResponse


class Last(object):
    def __init__(self, request):
        """
        Initialize the box.
        """
        self.session = request.session
        box = self.session.get(settings.LAST_SEEN_SESSION_ID)
        if not box:
            # save an empty box in the session
            box = self.session[settings.LAST_SEEN_SESSION_ID] = {}
        self.box = box

    def add(self, product_id):
        """
        Add a product to the box or update its quantity.
        """
        if product_id not in self.box:
            if len(self.box) > 10:
                del self.box[0]
            self.box[product_id] = product_id
        
        self.save()
    
    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the box.
        """
        product_id = str(product.id)
        if product_id in self.box:
            del self.box[product_id]
            self.save()

    def clear(self):
        # remove box from session
        del self.session[settings.LAST_SEEN_SESSION_ID]
        self.save()