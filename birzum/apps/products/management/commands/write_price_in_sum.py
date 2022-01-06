from decimal import Decimal

from django.core.management.base import BaseCommand

from birzum.apps.smallapps.rating.models import Currency

from ...models import Product


class Command(BaseCommand):

    """
    item item has price field completed
    complete price_sum field as well according to usd rate
    ------------------------------------------------------
    item item has discount_price field completed
    complete discount_price_sum field as well according to usd rate
    """

    usd_course = Currency.objects.last()
    products = Product.objects.all()

    def handle(self, *args, **options):
        # if currency model has a record in it, then update

        if self.usd_course:
            for item in self.products:
                # item item has price field completed
                # complete price_sum field as well according to usd rate
                if item.price:
                    item.price_sum = round(item.price * self.usd_course.currency, 2)

                # item item has price field completed
                # complete price_sum field as well according to usd rate
                if item.discount_price:
                    item.discount_price_sum = round(item.discount_price * self.usd_course.currency, 2)

                item.save()

            print("Prices has been updated successfully")

        else:
            print("Get a USD rate first, type: [python manage.py update_usd]")
