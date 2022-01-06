from django import template

from birzum.apps.smallapps.rating.models import Currency

register = template.Library()


@register.filter(name='addstr')
def add_str(s1, s2):
    return str(s1) + str(s2)


@register.inclusion_tag("templatetags/banner_info.html")
def get_banner_info(info):

    return {
        "red": info.split(" ")[0],
        "black": " ".join(info.split(" ")[1:]), 
    }


@register.filter(name="sum")
def do_sum(number):
    price = Currency.objects.all().last()
    try:
        return int((float(price.currency) * float(number)))
    except:
        return number
