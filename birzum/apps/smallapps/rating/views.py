from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from birzum.apps.products.models import Product
from .models import Rating
# Create your views here.


def rate(request, id):
    point = request.GET.get('rate')
    product = get_object_or_404(Product, id=id)
    if product:
        Rating.objects.create(product=product, rate=int(point))

    ratings = Rating.objects.filter(product=product)
    overall = int(round(ratings.aggregate(Avg('rate'))['rate__avg']))
    product.rating = overall
    product.save()
    data = {'exists': False, 'rate': int(point), 'overall': overall}

    return JsonResponse(data)
