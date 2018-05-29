from django.utils.safestring import mark_safe
from django import template
import json


register = template.Library()


@register.filter
def to_spaces(string):
    return string.replace('_', ' ')


@register.filter
def as_json(data):
    return mark_safe(json.dumps(data))
