import json

from django.core.management.base import BaseCommand

from birzum.apps.products.models import Category

class Command(BaseCommand):

    """
    populate category model
    """

    cats = Category.objects.all()

    def populate_fields(self, cats):
        for item in self.cats:
            item.name = cats[item.pk]['name']
            item.save()
        print("Job completed!")

    def handle(self, *args, **options):
        print('Getting categories.json from fixtures...')
        with open('fixtures/categories.json', 'r') as categories:
            categories = json.load(categories)

        cats = {}
        print('generating simple dict for storing categories data sturctured...')
        for item in categories:
            cats[item['pk']] = item['fields']

        print('Populating fields...')
        self.populate_fields(cats)
