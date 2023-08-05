from markdownify import markdownify as md

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='markdownify')
@stringfilter
def markdownify(value, *args):
    """Converts a HTML string to Markdown using markdownify"""
    return md(value, *args)