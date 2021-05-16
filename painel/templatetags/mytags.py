from django import template
from datetime import datetime


register = template.Library()


@register.simple_tag
def current_time(format_string):
    time =  datetime.now().strftime(format_string)
    return time
