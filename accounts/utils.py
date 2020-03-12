from .models import Student

def get_current_student(request):
    try:
        return Student.objects.get(user__username=request.user.username)
    except Student.DoesNotExist:
        return None