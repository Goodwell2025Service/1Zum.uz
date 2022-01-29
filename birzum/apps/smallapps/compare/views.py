from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _

from birzum.apps.products.models import Product 
from .compare import Compare


def compare_add(request, id):
    # xaridorga ko'rasiladigon xabarlar
    success_message = _("Mahsulot muvoffaqiyatli qo'shildi!")
    fail_message = _("Mahsulot sotuvda qolmagan!")

    compare = Compare(request)
    obj = Product.objects.filter(id=id).first()

    # agar product bor bo'lsa get parametrdan uni countini tekshirib ko'ramiz
    if obj:
        print("Compareaga qoshildi")
        # tekshiruv tugagandan song compareaga mahsulotni qo'shib yuboramiz
        compare.add(str(obj.id))

        return JsonResponse({"success": True, "message": success_message}, safe=False)

    return JsonResponse({"success": False, "message": fail_message}, safe=False)


def compare_remove(request, product_id):
    compare = Compare(request)
    product = get_object_or_404(Product, id=product_id)
    compare.remove(str(product.id))
    return redirect('compare:compare')


def compare_clear(request):
    compare = Compare(request)
    compare.clear()
    return redirect('compare:compare')


def compare_detail(request):
    compare = Compare(request)
    products = Product.objects.filter(id__in=compare.compare.keys())
    return render(request, 'smallapps/compare/compare.html', {'products': products})
