from .utils import get_current_student

class StudentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        student = get_current_student(request)
        response.context_data['student'] = student
        return response