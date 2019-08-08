from django import template

register = template.Library()


@register.simple_tag
def get_field_label(obj, name):
    return obj._meta.get_field(name).verbose_name.title()


@register.simple_tag
def get_field_value(obj, name):
    return getattr(obj, name)


@register.filter
def is_odd(number):
    return number % 2 != 0
