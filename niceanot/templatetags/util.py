from django import template
from niceanot import *

register = template.Library()


@register.simple_tag
def get_site_title():
    return site_title
