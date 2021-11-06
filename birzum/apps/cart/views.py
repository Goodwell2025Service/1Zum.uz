from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from birzum.apps.products.models import Product

from .cart import Cart


@require_POST
def cart_add(request):
    print(" ------------------------------- \n\
        fucking shit are you doing something or not \n ---------------------------")
    if request.method == "POST":
        print("method is pooooost")
        return HttpResponse("fuck you it has worked")
    print(" This is a fucking get method")
    return JsonResponse({"response": request.method}, safe=False)


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
    return render(request, 'cart/cart.html')
