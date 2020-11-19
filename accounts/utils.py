from .models import Student
from .models import Teacher
from .models import User


def is_student(request):
    if not request.user.is_authenticated: return False
    return User.objects.get(username=request.user.username).is_student

def is_teacher(request):
    if not request.user.is_authenticated: return False
    return User.objects.get(username=request.user.username).is_teacher

def get_current_student(request):
    if not is_student(request): return None
    return Student.objects.get(user__username=request.user.username)

def get_current_teacher(request):
    if not is_teacher(request): return None
    return Teacher.objects.get(user__username=request.user.username)
