from django import template
import json
import hashlib

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter(name='jsonify')
def jsonify(data):
    if isinstance(data, dict):
        return data
    else:
        return json.loads(data)

COLOR_LIST = [
    ('#A13D63', 'white'),
    ('#9FC490', 'default'),
    ('#011936', 'white'),
    ('#B0413E', 'white'),
    ('#FBD87F', 'default'),
    ('#34113F', 'white'),
    ('#86E7B8', 'default'),
    ('#424651', 'white'),
    ('#FDFDFF', 'default'),
    ('#AD8A64', 'white'),
    ('#457B9D', 'white'),
    ('#E63946', 'white'),
]

@register.simple_tag
def course_color(text):
    hex_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
    int_hash = int(hex_hash, 16)
    return COLOR_LIST[int_hash % len(COLOR_LIST)]

