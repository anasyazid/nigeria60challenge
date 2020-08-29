from django import template

register = template.Library()

@register.filter
def percentage(num, denom):
    return round((num / denom) * 100, 2)