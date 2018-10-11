from django import template

register = template.Library()

@register.filter(name='in')
def has(value, _list):
    return value in _list
