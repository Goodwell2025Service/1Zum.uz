from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from birzum.apps.cart.cart import Cart

from .models import Order
from .utils import create_order_items


# Create your views here.
class OrderCreate(CreateView):
    model = Order

    fields = [
        'first_name', 'last_name', 'region', 'district', 'house',
        'street', 'postcode', 'phone', 'message'
        ]

    template_name = 'order/order_create.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        if form.is_valid:
            extra = self.request.POST
            obj = form.save()
            obj.payment = extra.get('payment-method', '')
            obj.shipping = extra.get('shipping-method', '')
            obj.save()
            create_order_items(obj=obj, cart=cart, request=self.request)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("order:success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context
    

order_create_view = OrderCreate.as_view()


class OrderSucceeded(TemplateView):
    template_name = "order/success.html"


order_succeeded_view = OrderSucceeded.as_view()
