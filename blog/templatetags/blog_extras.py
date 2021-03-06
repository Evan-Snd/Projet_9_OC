from django import template
from typing import Union

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.filter(name='range')
def filter_range(start, end: Union[int, str]):
    if isinstance(end, str):
        end_nb = int(end)
    else:
        end_nb = end
    return range(start, end_nb)
