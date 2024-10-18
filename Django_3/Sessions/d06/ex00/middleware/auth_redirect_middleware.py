from django.shortcuts import redirect
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin

class AuthRedirectMiddleware(MiddlewareMixin):
    def process_requst(self, request: HttpRequest):
        if request.user.is_authenticated and request.path in ['/subscription/', '/login/']:
            return redirect('/')