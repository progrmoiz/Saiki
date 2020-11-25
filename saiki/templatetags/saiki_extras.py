from assignment.models import AssignmentWork
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
    ('#A13D63', 'white', '#ffffff'),
    ('#34113F', 'white', '#ffffff'),
    ('#AD8A64', 'white', '#ffffff'),
    ('#FDFDFF', 'default', '#000000'),
    ('#86E7B8', 'default', '#000000'),
    ('#9E2A2B', 'white', '#ffffff'),
    ('#335C67', 'white', '#ffffff'),
    ('#011936', 'white', '#ffffff'),
    ('#9FC490', 'default', '#000000'),
    ('#B0413E', 'white', '#ffffff'),
    ('#FBD87F', 'default', '#000000'),
    ('#424651', 'white', '#ffffff'),
    ('#457B9D', 'white', '#ffffff'),
]

@register.simple_tag
def get_assignment_work(assignment, student):
    return AssignmentWork.objects.filter(assignment=assignment, student=student).first()

@register.simple_tag
def course_color(text):
    hex_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
    int_hash = int(hex_hash, 16)
    return COLOR_LIST[int_hash % len(COLOR_LIST)]

@register.simple_tag
def post_color(t, **kwargs):
    if t == 'assignment':
        return ('#6BAA75', 'white', '#ffffff', '#dee2e6')
    else:
        return ('#ffffff', 'default', '#000000', '#8898aa')

@register.simple_tag
def app_color(t, **kwargs):
    if t == 'assignment':
        return ('#6BAA75', 'white', '#ffffff')
    if t == 'announcement':
        return ('#202C59', 'white', '#ffffff')
    if t == 'result':
        return ('#38AECC', 'white', '#ffffff')
    elif t == 'course':
        return course_color(kwargs['text'])
    else:
        return None