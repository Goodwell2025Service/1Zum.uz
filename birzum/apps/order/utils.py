from django.conf import settings

from .models import OrderItem


def replace_commas(number):
   return str(number).replace(',', '  ')


def send_telegram_notify(message):
    if not settings.DEBUG:
        group_id = settings.TELEGRAM_GROUP_ID
        bot_token = settings.TELEGRAM_NOTIFY_BOT_ID

        action = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + group_id + \
                '&parse_mode=html&text=' + message


def create_order_items(obj, cart, request=None):
    products = ""
    for item in cart:
        price = replace_commas("{:,.2f}".format(item['price']))
        products += "Модель: " + str(item['product'].title) + \
                ",\nЦена: " + price + " сум,\nКоличество: " + \
                str(item['quantity']) + ",\n" \
                "\n------------\n"

        OrderItem.objects.create(
            order=obj,
            product=item['product'],
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
