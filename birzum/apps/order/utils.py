import requests

from django.conf import settings
from decimal import Decimal
from .models import OrderItem
from birzum.apps.products.models import Product


def replace_commas(number):
   return str(number).replace(',', '  ')


def send_telegram_notify(message):
    if not settings.DEBUG:
        group_id = settings.TELEGRAM_CHAT_ID
        bot_token = settings.TELEGRAM_BOT_TOKEN

        print(bot_token, group_id)

        action = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + group_id + \
                '&text=' + message
        
        response = requests.get(action)
        print("success -", response.status_code)

def create_order_items(obj, cart, request=None):
    products = ""
    print("Telegramga jo'natmoqchi")
    for item in cart:
        price = replace_commas("{:,.2f}".format(Decimal(item['price'])))
        products += "Модель: " + str(item['product']['title']) + \
                ",\nЦена: " + price + " сум,\nКоличество: " + \
                str(item['quantity']) + ",\n" \
                "\n------------\n"

        product = Product.objects.filter(id=item['product']['id']).first()

        OrderItem.objects.create(
            order=obj,
            product=product,
            price=item['price'],
            quantity=item['quantity']
        )

    sent = obj.id
    link_order = '/ru/way2020passNum00/orders/order/' + str(sent) + '/change/'
    name, phone = f"{obj.first_name} {obj.last_name}", obj.phone

    message = f"У вас новый заказ 🎉 \n\n" + \
    "🧔 - {name}\n📞 - {phone}\n\n"+ \
    "Продукты:\n{products}\n\n "+\
    "Посмотреть заказ на сайте 👇 {link_order}"

    send_telegram_notify(message)

    cart.clear()
