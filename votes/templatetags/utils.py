from django import template

register = template.Library()


@register.simple_tag
def percentage(polls, id, total_count):
    try:
        return (get_count(polls, id) / total_count) * 100
    except ZeroDivisionError:
        return 0


@register.filter
def get_count(polls, id):
    for poll in polls:
        if poll['design_id'] == id:
            return poll['votes']
    return 0
