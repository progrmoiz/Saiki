from .models import Student

def get_current_student(request):
    return Student.objects.get(user__username=request.user.username)