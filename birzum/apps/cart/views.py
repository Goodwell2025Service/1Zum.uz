from django.core.checks import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.utils.translation import gettext_lazy as _

from birzum.apps.products.models import Product

from .cart import Cart


def cart_add(request, id):
    # xaridorga ko'rasiladigon xabarlar
    success_message = _("Mahsulot muvoffaqiyatli qo'shildi!")
    fail_message = _("Mahsulot sotuvda qolmagan!")

    cart = Cart(request)
    count = request.GET.get('count')
    obj = Product.objects.filter(available=True, id=id).first()

    # agar product bor bo'lsa get parametrdan uni countini tekshirib ko'ramiz
    if obj:
        try:
            count = int(count)
        except:
            count = 1

        # tekshiruv tugagandan song cartaga mahsulotni qo'shib yuboramiz
        cart.add(product=obj, quantity=count, update_quantity=False)
        
        return JsonResponse({"success": True, "message": success_message}, safe=False)

    return JsonResponse({"success": False, "message": fail_message}, safe=False)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:detail')


def cart_detail(request):
    cart = Cart(request)
    print("#############################")
    print(cart.cart)
    return render(request, 'cart/cart.html')
