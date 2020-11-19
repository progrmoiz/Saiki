from .utils import get_current_student, get_current_teacher, is_student, is_teacher

class AccountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        student = get_current_student(request)
        teacher = get_current_teacher(request)
        
        response.context_data['student'] = student
        response.context_data['teacher'] = teacher
        
        response.context_data['is_student'] = is_student(request)
        response.context_data['is_teacher'] = is_teacher(request)

        return response