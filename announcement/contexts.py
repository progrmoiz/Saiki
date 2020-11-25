def notification(request):
    if not request.user.is_authenticated: return {}

    return {
        'unread_notifications': request.user.notifications.unread()[:5]
    }