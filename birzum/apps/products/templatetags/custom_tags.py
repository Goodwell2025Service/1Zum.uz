from django import template

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
