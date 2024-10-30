# news/templatetags/custom_tags.py
from django import template

register = template.Library()

# Custom Filter
@register.filter(name='truncate_chars')
def truncate_chars(value, num):
    """Truncate a string to the specified number of characters."""
    if len(value) > num:
        return value[:num] + '...'
    return value

# Custom Tag
@register.simple_tag
def multiply(value, arg):
    """Multiply the given value by the argument."""
    return value * arg
