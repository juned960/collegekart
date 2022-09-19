from django import template
from math import floor

register = template.Library()


@register.simple_tag
def selected_attr(request__slug ,slug):
    if request__slug ==slug:
        return "selected"
    else:
        return ''
    
        
 