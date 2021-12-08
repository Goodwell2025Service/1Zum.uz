from django import template

register = template.Library()


@register.filter(name='addstr')
def add_str(s1, s2):
    return str(s1) + str(s2)
