from .models import Student
from .models import Teacher
from .models import User

def is_student(request):
    if not request.user.is_authenticated: return False
    return request.user.is_student

def is_teacher(request):
    if not request.user.is_authenticated: return False
    return request.user.is_teacher

def get_current_student(request):
    if not is_student(request): return None
    return Student.objects.get(user__username=request.user.username)

def get_current_teacher(request):
    if not is_teacher(request): return None
    return Teacher.objects.get(user__username=request.user.username)

def account_context_processor(request):
     return {
        'is_student': is_student(request),
        'is_teacher': is_teacher(request),
        'student': get_current_student(request),
        'teacher': get_current_teacher(request)
     }