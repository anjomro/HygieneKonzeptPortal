from django.conf import settings


def env_vars(request):
    return {
        "title": settings.TITLE,
        "name": settings.NAME,
        "adress": settings.ADRESS,
        "email": settings.EMAIL,
        "email_link": settings.EMAIL_LINK
    }
