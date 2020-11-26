from assignment.models import AssignmentWork
from django import template
from saiki.utils import get_course_color
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


@register.simple_tag
def get_assignment_work(assignment, student):
    return AssignmentWork.objects.filter(assignment=assignment, student=student).first()

@register.simple_tag
def course_color(text):
    return get_course_color(text)

@register.simple_tag
def post_color(post_type, **kwargs):
    if post_type == 'assignment':
        return ('#6BAA75', 'white', '#ffffff', '#f8f9fe')
    else:
        return ('#ffffff', 'default', '#172b4d', '#8898aa')

@register.simple_tag
def app_color(t, **kwargs):
    if t == 'assignment':
        return ('#6BAA75', 'white', '#ffffff', '#f8f9fe')
    if t == 'announcement':
        return ('#202C59', 'white', '#ffffff', '#ced4da')
    if t == 'result':
        return ('#38AECC', 'white', '#ffffff', '#ced4da')
    elif t == 'course':
        return course_color(kwargs['text'])
    else:
        return None