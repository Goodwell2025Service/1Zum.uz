import json

from django.core.management.base import BaseCommand

from birzum.apps.products.models import Product

class Command(BaseCommand):

    """
    populate category model
    """

    pros = Product.objects.all()

    def populate_fields(self, pros):
        for item in self.pros:
            item.title = pros[item.pk]['title']
            item.description = pros[item.pk]['description']
            item.specs = pros[item.pk]['specs']
            item.save()
        print("Job completed!")

    def handle(self, *args, **options):
        print('Getting products.json from fixtures...')
        with open('fixtures/products.json', 'r') as products:
            products = json.load(products)

        pros = {}
        print('generating simple dict for storing products data sturctured...')
        for item in products:
            pros[item['pk']] = item['fields']

        print('Populating fields...')
        self.populate_fields(pros)
