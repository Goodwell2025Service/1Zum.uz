import datetime
import json
import logging
import urllib.request
import requests
from datetime import timedelta

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from ...models import Currency


class Command(BaseCommand):

    def handle(self, *args, **options):
        max_retries = 5
        url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json'
        tried = 0
        while True:
            try:
                resp = requests.get(url)
                data = resp.json()
                query = Currency.objects.all().last()
                if query:
                    query.currency = float(data[0]['Rate'])
                    query.updated = timezone.now()
                    query.save()
                else:
                    query = Currency.objects.create(
                        currency=float(data[0]['Rate']),
                        updated=timezone.now()
                    )

                return False
            except Exception as e:
                logging.error('Exception while updating currency values %s' % e)
                tried += 1
                if tried >= max_retries:
                    break

            logging.warning('Could not update currency values after %s attempts' % max_retries)
