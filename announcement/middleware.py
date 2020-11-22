
class NotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):

        if not request.path.startswith('/api/'):
            if request.user.is_authenticated:
                response.context_data['unread_notifications'] = request.user.notifications.unread()[:5]

        return response