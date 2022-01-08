from django.contrib import messages
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.utils.translation import gettext_lazy as _

from birzum.apps.products.models import Product
from .models import Rating
# Create your views here.


def rate(request, id):
    rating = request.POST.get('review[rating]', 0)
    message = request.POST.get('message', "")
    phone = request.POST.get('phone', "")
    name = request.POST.get('name', "")

    print(rating, message, phone, name)
    product = get_object_or_404(Product, id=id)
    if product:
        Rating.objects.create(
            product=product, rate=int(rating), comment=message,
            person=name, contact=phone
            )

        messages.add_message(request, messages.SUCCESS, _("Mahsulotga baho berganingizdan mamnunmiz!"))

    ratings = Rating.objects.filter(product=product)
    overall = int(round(ratings.aggregate(Avg('rate'))['rate__avg']))
    product.rating = overall
    product.save()

    return redirect('products:detail', cat_slug=product.category.slug, slug=product.slug)
