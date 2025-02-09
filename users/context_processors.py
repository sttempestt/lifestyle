from django.contrib.auth.models import User

def add_user_to_context(request):
    return {
        'user': request.user if request.user.is_authenticated else None
    }
