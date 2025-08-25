# myapp/middleware.py
from django.utils import translation

class AdminRussianMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            translation.activate('ru')
            request.LANGUAGE_CODE = 'ru'
        response = self.get_response(request)
        return response
