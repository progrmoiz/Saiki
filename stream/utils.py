from avatar.utils import get_primary_avatar, get_default_avatar_url

def get_avatar_url(comment):
    if comment.user is not None:
        try:
            return get_primary_avatar(comment.user, 36).get_absolute_url()
        except Exception as exc:
            pass
    return get_default_avatar_url()
