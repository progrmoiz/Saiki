from .utils import is_student, is_teacher, get_current_student, get_current_teacher

def account(request):
     return {
        'is_student': is_student(request),
        'is_teacher': is_teacher(request),
        'student': get_current_student(request),
        'teacher': get_current_teacher(request)
     }