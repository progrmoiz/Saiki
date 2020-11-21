from django import template
import hashlib

register = template.Library()

COLOR_LIST = [
    ('#9FC490', 'light'),
    ('#011936', 'dark'),
    ('#A13D63', 'dark'),
    ('#B0413E', 'dark')
]

@register.simple_tag
def course_color(text):
    hex_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
    int_hash = int(hex_hash, 16)
    return COLOR_LIST[int_hash % len(COLOR_LIST)]

