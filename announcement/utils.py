def notification_context_processor(request):
    if not request.user.is_authenticated: return {}

    return {
        'unread_notifications': request.user.notifications.unread()[:5]
    }