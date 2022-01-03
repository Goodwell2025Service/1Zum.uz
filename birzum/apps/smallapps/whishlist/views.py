from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _

from birzum.apps.products.models import Product 
from .whishlist import Whishlist


def whishlist_add(request, id):
    # xaridorga ko'rasiladigon xabarlar
    success_message = _("Mahsulot muvoffaqiyatli qo'shildi!")
    fail_message = _("Mahsulot sotuvda qolmagan!")

    whishlist = Whishlist(request)
    obj = Product.objects.filter(available=True, id=id).first()

    # agar product bor bo'lsa get parametrdan uni countini tekshirib ko'ramiz
    if obj:
        print("Whishlistaga qoshildi")
        # tekshiruv tugagandan song whishlistaga mahsulotni qo'shib yuboramiz
        whishlist.add(str(obj.id))

        return JsonResponse({"success": True, "message": success_message}, safe=False)

    return JsonResponse({"success": False, "message": fail_message}, safe=False)


def whishlist_remove(request, product_id):
    whishlist = Whishlist(request)
    product = get_object_or_404(Product, id=product_id)
    whishlist.remove(str(product.id))
    return redirect('whishlist:whishlist')


def whishlist_clear(request):
    whishlist = Whishlist(request)
    whishlist.clear()
    return redirect('whishlist:whishlist')


def whishlist_detail(request):
    whishlist = Whishlist(request)
    products = Product.objects.filter(id__in=whishlist.whishlist.keys())
    return render(request, 'smallapps/whishlist/whishlist.html', {'products': products})
