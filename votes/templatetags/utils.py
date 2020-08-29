from django import template

register = template.Library()


@register.filter
def percentage(num, denom):
    try:
        return round((num / denom) * 100, 2)
    except TypeError:
        return -0
